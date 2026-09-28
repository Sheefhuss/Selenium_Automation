# Module 1: Core Fundamentals, Locators & Advanced Interactions

This module covers foundational Selenium automation concepts, moving from basic element locators and explicit waits to advanced browser interactions like alerts, web tables, and frames.

---
## 📹 Video Demonstration
* **Watch the Module 1 Walkthrough:** [Click here to view the video demonstration](https://drive.google.com/file/d/1Hc-3GKYIXKfSCKTEQqbLd7NVYQbQJt2B/view?usp=drivesdk)

---

## 📋 Assignment Overview

### Tier 1: Core Fundamentals & Locators
* **Assignment 1: The Multi-Locator Challenge**
  * **Task:** Navigate to a login page, interact with the username field using `By.ID`, password using `By.NAME`, and login button using `By.XPATH`.
  * **Validation:** Assert the final URL contains `/inventory.html`.
* **Assignment 2: Synchronization & Explicit Waits**
  * **Task:** Handle dynamic content using `WebDriverWait` and `expected_conditions` instead of `time.sleep()`.
* **Assignment 3: (Internal Practice)**
  * Core helper script or additional practice exercise.

### Tier 2: Advanced User Interactions
* **Assignment 4: JavaScript Alerts and Confirms**
  * **Task:** Trigger, accept, dismiss, and input text into JavaScript Alerts, Confirm boxes, and Prompt boxes using `driver.switch_to.alert`.
* **Assignment 5: The HTML Web Table Extractor**
  * **Task:** Iterate through dynamic multi-column tables, match specific rows by name, and retrieve target values (e.g., status/price).
* **Assignment 6: Windows, Tabs, and Iframes**
  * **Task:** Switch contexts between embedded iframes and multiple browser tabs using `window_handles` and `switch_to.frame()`.

---

## 📦 Installation & Setup

1. **Clone or navigate to your project workspace.**
2. **Install the required dependencies:**
   Make sure you have Python installed, then run the following command in your terminal:
   ```bash
   pip install -r requirements.txt
