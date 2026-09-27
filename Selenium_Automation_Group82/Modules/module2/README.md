# Module 2: Page Object Model, Data-Driven Testing & PyTest

This module advances automation architecture by implementing the Page Object Model (POM), data-driven testing (DDT) using external files, and scalable test execution using PyTest with HTML reporting.

---

## 📹 Video Demonstration
* **Watch the Module 2 Walkthrough:** [Click here to view the video demonstration](https://drive.google.com/file/d/1wvSgMq75kBy-l2QaSVnMi0MIKBuMpG9j/view?usp=drivesdk)

---

## 📋 Assignment Overview

* **Assignment 7: Page Object Model (POM) Restructure**[cite: 3]
  * **Task:** Restructure your working scripts from Tier 1 into a Page Object Model design pattern[cite: 3].
  * **Architecture:** Create separate page classes (e.g., `LoginPage`, `DashboardPage`) containing only locator definitions and UI methods, keeping actual test assertions completely separate from the locators[cite: 3].
* **Assignment 8: Data-Driven Automation (DDT)**[cite: 3]
  * **Task:** Build a login script that reads multiple test cases from an external source, such as an Excel file via pandas or a local JSON/CSV file[cite: 3].
  * **Execution:** Loop through the test data to execute combinations of correct and incorrect usernames and passwords, asserting that proper validation errors appear for each case[cite: 3].
* **Assignment 9: PyTest Integration with HTML Reporting**[cite: 3]
  * **Task:** Convert your setup to run via PyTest[cite: 3].
  * **Implementation:** Use PyTest fixtures for browser initialization and teardown. Run your test suite from the terminal and configure it to auto-generate an HTML execution report with embedded screenshots of any failed test steps[cite: 3].

---

## 📦 Installation & Setup

1. **Clone or navigate to your project workspace.**
2. **Install the required dependencies:**
   Ensure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt