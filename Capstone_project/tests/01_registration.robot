*** Settings ***
Resource    ../resources/common.resource
Resource    ../resources/registration_page.resource

Suite Setup       Open Application
Suite Teardown    Close Application
Test Teardown     Take Test Screenshot

*** Test Cases ***
Create New Account
    [Documentation]    Runs only ONCE ever. Skipped once registration_done.flag exists.
    ${done}=    Registration Already Done
    Skip If    ${done}    Already registered earlier - skipping.
    Open Signup Page
    Enter Signup Details
    Fill Account Information
    Create Account
    Verify Account Created
    Mark Registration Done
