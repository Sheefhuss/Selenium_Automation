# Capstone Project: Web UI Test Automation (Robot Framework)

Automated end-to-end UI tests for the e-commerce practice site
[Automation Exercise](https://automationexercise.com), built with
**Robot Framework** and **SeleniumLibrary** using the **Page Object / resource-file** pattern.

---

## Demonstration Video

> **Demo link:** _paste_
---

## Table of Contents

1. [Overview](#1-overview)
2. [Project Structure](#2-project-structure)
3. [Prerequisites and Installation](#3-prerequisites-and-installation)
4. [Configuration](#4-configuration)
5. [How to Run](#5-how-to-run)
6. [Test Suites](#6-test-suites)
7. [Run-Once Registration Logic](#7-run-once-registration-logic)
8. [Resource Files and Keyword Reference](#8-resource-files-and-keyword-reference)
9. [Screenshots and Reports](#9-screenshots-and-reports)
10. [Troubleshooting](#10-troubleshooting)

---

## 1. Overview

The project automates the main user journey of an online shop:

| Order | Feature | What is verified |
|-------|---------|------------------|
| 1 | Registration | A new account can be created (runs **once only**) |
| 2 | Login | The registered user can log in (runs **every time**) |
| 3 | Products | A product can be searched and appears in the results |
| 4 | Cart | A product can be added and the cart page is shown |
| 5 | Checkout | The user can proceed from the cart to checkout |

Key design points:

- **Separation of concerns:** test cases (`tests/`) only describe *what* is tested; the *how*
  (locators and browser actions) lives in reusable keywords (`resources/`).
- **Ordered execution:** suite files are numbered so they always run in the same order.
- **Run-once registration:** a flag file stops registration from re-running once the account exists.
- **Evidence:** one screenshot is captured per test, plus Robot Framework's HTML report and log.

---

## 2. Project Structure

```
Capstone_project/
|
|-- README.md                      <- this documentation
|-- registration_done.flag         <- created automatically after registration succeeds
|
|-- tests/                         <- test suites (what is tested)
|   |-- 01_registration.robot
|   |-- 02_login.robot
|   |-- 03_products.robot
|   |-- 04_cart.robot
|   `-- 05_checkout.robot
|
|-- resources/                     <- reusable keywords and locators (how it is tested)
|   |-- common.resource            <- shared settings, browser open/close, flag, screenshots
|   |-- registration_page.resource
|   |-- login_page.resource
|   |-- product_page.resource
|   `-- cart_page.resource
|
`-- results/                       <- generated on every run
    |-- output.xml
    |-- log.html
    |-- report.html
    `-- screenshots/               <- one .png per test
```

> Suite files are named `01_`, `02_`, ... because Robot Framework runs files in a folder in
> alphabetical order. The numeric prefix guarantees registration always comes first.

---

## 3. Prerequisites and Installation

- **Python 3.8+**
- **Google Chrome** (Selenium 4.6+ downloads the matching driver automatically)
- **Robot Framework 5.0+** (uses `Skip If` and `IF` blocks)

```powershell
# optional: create and activate a virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# install dependencies
pip install robotframework robotframework-seleniumlibrary

# verify
robot --version
```

---

## 4. Configuration

All shared settings are in `resources/common.resource` under `*** Variables ***`:

| Variable | Default | Purpose |
|----------|---------|---------|
| `${URL}` | `https://automationexercise.com` | Site under test |
| `${BROWSER}` | `chrome` | Browser used |
| `${USER_EMAIL}` | `test_12345@gmail.com` | Email used for **both** registration and login |
| `${USER_PASSWORD}` | `Password123` | Password used for registration and login |
| `${USER_NAME}` | `Your_Name` | Name entered on the signup form |
| `${FLAG_FILE}` | `<run folder>/registration_done.flag` | Marks that registration is complete |

Because registration and login both read `${USER_EMAIL}` and `${USER_PASSWORD}`, they always
refer to the same account. Change credentials in one place only.

---

## 5. How to Run

**Always run from the `Capstone_project` folder**, because the flag file is created in the
folder you run from.

```powershell
# run for everything, in order
robot --outputdir results tests

# run a single suite
robot --outputdir results tests/02_login.robot

# run by test name
robot --outputdir results --test "Login With Valid Credentials" tests
```

After the run, open `results/report.html` (summary) or `results/log.html` (step-by-step detail).

---

## 6. Test Suites

Every suite uses the same lifecycle:

- **Suite Setup:** `Open Application` (opens a fresh Chrome window)
- **Test Teardown:** `Take Test Screenshot`
- **Suite Teardown:** `Close Application`

Each suite starts in a **new browser session**, so the user always begins logged out.

| File | Test case | Steps |
|------|-----------|-------|
| `01_registration.robot` | Create New Account | Check flag (skip if present) -> Open Signup Page -> Enter Signup Details -> Fill Account Information -> Create Account -> Verify Account Created -> Mark Registration Done |
| `02_login.robot` | Login With Valid Credentials | Open Login Page -> Enter Login Details -> Click Login -> Verify User Is Logged In |
| `03_products.robot` | Search For Product | Open Products Page -> Search Product `Blue Top` -> Verify Product Is Displayed |
| `04_cart.robot` | Add Product To Cart | Open Products Page -> Add First Product To Cart -> Open Cart -> Verify Cart Is Displayed |
| `05_checkout.robot` | Proceed To Checkout | Open Products Page -> Add First Product To Cart -> Open Cart -> Verify Cart Is Displayed -> Proceed To Checkout |

---

## 7. Run-Once Registration Logic

An account can only be registered once (the site rejects an email that already exists), so
registration must not repeat on later runs, while login must run every time.

```
Run starts
   |
   v
Does registration_done.flag exist?
   |-- No  --> run registration --> success --> create flag --> Login runs
   `-- Yes --> registration is SKIPPED ------------------------> Login runs
```

- The flag is written **only after** the account-created page is verified. If registration
  fails, no flag is created and the next run tries again.
- A skipped test shows as `SKIP` in the report. This is intentional, not a failure.

**Registering a different account**

1. Change `${USER_EMAIL}` in `resources/common.resource` to a new, unused email.
2. Delete the flag: `Remove-Item registration_done.flag`

The flag only checks whether the file exists; it does not compare emails. If you change the
email but keep the flag, registration is skipped and login fails because that account was
never created.

**If the account already exists** (for example from an earlier manual run), create the flag by hand:

```powershell
New-Item registration_done.flag -ItemType File
```

---

## 8. Resource Files and Keyword Reference

### `common.resource`: shared settings and helpers

| Keyword | Description |
|---------|-------------|
| `Open Application` | Opens `${URL}` in `${BROWSER}`, maximizes the window, and sets the screenshot folder to `results/screenshots`. |
| `Close Application` | Closes all open browsers. |
| `Registration Already Done` | Returns `True` if `registration_done.flag` exists, otherwise `False`. |
| `Mark Registration Done` | Creates `registration_done.flag`. |
| `Take Test Screenshot` | Saves a screenshot named `<suite>_<test>_<status>.png`. Skipped tests are not captured. |

### `registration_page.resource`

| Keyword | Description |
|---------|-------------|
| `Open Signup Page` | Clicks the "Signup / Login" link (via JavaScript to avoid overlay clicks) and waits for the name field. |
| `Enter Signup Details` | Enters name and email, clicks Signup, waits for the account form. |
| `Fill Account Information` | Fills password, first/last name, address, state, city, zip code and mobile number. |
| `Create Account` | Clicks Create Account and waits for the `account_created` page. |
| `Verify Account Created` | Asserts the URL contains `account_created`. |

### `login_page.resource`

| Keyword | Description |
|---------|-------------|
| `Open Login Page` | Clicks the "Signup / Login" link (via JavaScript) and waits for the login form. |
| `Enter Login Details` | Types `${USER_EMAIL}` and `${USER_PASSWORD}` into the login form. |
| `Click Login` | Clicks the Login button. |
| `Verify User Is Logged In` | Asserts the page contains "Logged in as". |

### `product_page.resource`

| Keyword | Description |
|---------|-------------|
| `Open Products Page` | Navigates to `/products` and waits for the search box. |
| `Search Product` `${product}` | Types the product name and clicks the search button. |
| `Verify Product Is Displayed` `${product}` | Asserts the page contains the product name. |
| `Add First Product To Cart` | Adds the first product (`data-product-id='1'`) to the cart using JavaScript. |
| `Open Cart` | Navigates to `/view_cart` and waits for "Shopping Cart". |

### `cart_page.resource`

| Keyword | Description |
|---------|-------------|
| `Verify Cart Is Displayed` | Waits for the text "Shopping Cart" (up to 15 s). |
| `Proceed To Checkout` | Waits for the checkout button, scrolls to it, clicks it, and waits for "Checkout". |

---

## 9. Screenshots and Reports

Generated in `results/` on every run:

| Output | Location | Contents |
|--------|----------|----------|
| Report | `results/report.html` | High-level pass/fail/skip summary |
| Log | `results/log.html` | Step-by-step execution with embedded screenshots |
| Screenshots | `results/screenshots/` | One image per test, named with its PASS/FAIL status |
| Raw data | `results/output.xml` | Machine-readable results |

SeleniumLibrary also captures an automatic screenshot at the moment any step fails.

---

## 10. Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| `No keyword with name 'Close Application' found` | `common.resource` not imported or outdated | Use the `common.resource` from this project and check the `Resource` path in the suite |
| `Resource file ... does not exist` | Wrong relative path | Suites expect `../resources/`; keep the folder layout shown above |
| Registration fails at `id=password` | Email already registered | Create the flag by hand, or use a new email and delete the flag |
| Login fails after changing the email | Flag still present, so the new account was never created | Delete `registration_done.flag` and rerun |
| `ElementClickInterceptedException` on the login link | Browser extension or ad overlay covers the link | Links are clicked via JavaScript; also try running in an incognito profile without extensions |
| Registration runs again on every run | Robot run from a different folder | Always run from `Capstone_project` |
| Suites run in the wrong order | Files not numbered | Keep the `01_` to `05_` prefixes |
| `Skip If` or `IF` not recognized | Old Robot Framework | `pip install -U robotframework` |
| Old `tests.robot` errors | Leftover file from an earlier version | Delete it; only the five numbered suites are needed |

---

## Author

_Sheefa Hussain / Computer Science and Information Technology / 22-09-2026_
