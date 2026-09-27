# Selenium Automation — Wipro Programme Repository

**Sheefa Hussain** — Computer Engineering and Information Technology

This repository holds all deliverables for the Selenium automation programme:
weekly module workbooks (locators → advanced interactions → POM/DDT/PyTest →
BDD with Behave), the end-to-end **Capstone Project**, and course completion
certificates.

Each module and the Capstone project has its **own detailed README** inside
its folder. This top-level file is only a map — start here to see how
everything fits together, then open the folder you need.

---

## Repository Structure

```
Selenium_Automation/
│
├── README.md                     
│
├── Modules/                      <- weekly module workbooks
│   ├── requirements.txt          <- shared Python dependencies for Modules 1-3
│   │
│   ├── module1/                  <- Core Fundamentals, Locators & Advanced Interactions
│   │   ├── README.md
│   │   ├── code_session/         <- assignment1.py .. assignment6.py
│   │   ├── output/                <- screenshots per assignment
│   │   └── video_demonstration/
│   │
│   ├── module2/                  <- Page Object Model, Data-Driven Testing & PyTest
│   │   ├── README.md
│   │   ├── assignment7/          <- POM: login_page.py, test_login.py
│   │   ├── assignment8.py        <- DDT: reads login_data.csv
│   │   ├── login_data.csv
│   │   ├── test_assignment9.py   <- PyTest + HTML report
│   │   ├── report.html
│   │   └── output/                <- screenshots per assignment
│   │
│   └── module3/                  <- BDD with Behave
│       ├── README.md
│       ├── assignment1/features/         <- Behave + Selenium setup
│       ├── assignment2/features/         <- Data-driven Scenario Outline
│       └── assignment3/features/         <- Behave + Page Object Model
│
├── Capstone_project/              <- end-to-end Robot Framework test suite
│   ├── README (1).md              <- full Capstone documentation
│   ├── tests/                     <- 01_registration .. 05_checkout (numbered, run in order)
│   ├── resources/                 <- shared keywords, page objects, screenshot logic
│   ├── data/                      <- test_data.csv
│   ├── libraries/                 <- custom_library.py
│   ├── Jenkinsfile                <- CI pipeline definition
│   ├── registration_done.flag     <- created after first successful registration
│   └── results/                   <- log.html, report.html, output.xml, screenshots/
│
└── Certificates/                  <- course completion certificates (PDF)
    ├── Selenium Webdriver with Python.pdf
    ├── Python for Automation.pdf
    └── Coursera Test Automation with Robot Framework.pdf
```

---

## Modules Overview

| Module | Focus | Details |
|--------|-------|---------|
| **[Module 1](Modules/module1/README.md)** | Locators (`By.ID`/`NAME`/`XPATH`), explicit waits, JS alerts, web tables, windows/tabs/iframes | 6 assignments, each with its own script and output screenshot |
| **[Module 2](Modules/module2/README.md)** | Page Object Model restructure, data-driven testing with an external CSV, PyTest + auto-generated HTML report | 3 assignments (7-9) |
| **[Module 3](Modules/module3/README.md)** | Behavior-Driven Development with Behave: Gherkin scenarios, Scenario Outline data-driving, Behave + POM | 3 assignments |

Open each module's own README for the problem statement, objective, tools, and
result for every individual assignment — that level of detail isn't repeated
here.

---

## Capstone Project Overview

The **[Capstone Project](Capstone_project/README%20(1).md)** is a Robot
Framework + SeleniumLibrary test suite automating a full user journey on
[Automation Exercise](https://automationexercise.com):

1. **Registration** — runs once only; a flag file prevents re-registering an
   existing account on later runs.
2. **Login** — runs on every execution, using the same account created in
   step 1.
3. **Products** — search and verify a product.
4. **Cart** — add a product and open the cart.
5. **Checkout** — proceed from the cart to checkout.

Test suites live in `Capstone_project/tests/`, numbered `01_` to `05_` so they
always run in that order. Reusable keywords and locators are in
`Capstone_project/resources/`. Every run produces a full HTML report/log plus
one screenshot per test in `Capstone_project/results/`. Full setup and
run instructions are in the Capstone project's own README.

---

## Certificates

Course completion certificates for the underlying training are in
[`Certificates/`](Certificates/):

- Selenium WebDriver with Python
- Python for Automation
- Coursera — Test Automation with Robot Framework

---

## Getting Started

```powershell
# clone the repository
git clone https://github.com/Sheefhuss/Selenium_Automation.git
cd Selenium_Automation

# Modules 1-3 dependencies
pip install -r Modules/requirements.txt

# Capstone project dependencies
pip install robotframework robotframework-seleniumlibrary
```

Google Chrome is required for all Selenium-based runs (Selenium 4.6+
downloads the matching driver automatically).

To run the Capstone suite:
```powershell
cd Capstone_project
robot --outputdir results tests
```

To run a specific module assignment, see that module's own README for the
exact command (plain Python script, `pytest`, or `behave`, depending on the
module).

---

## Author

**Sheefa Hussain**
Computer Engineering and Information Technology
