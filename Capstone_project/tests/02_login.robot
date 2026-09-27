*** Settings ***
Resource    ../resources/common.resource
Resource    ../resources/login_page.resource

Suite Setup       Open Application
Suite Teardown    Close Application
Test Teardown     Take Test Screenshot

*** Test Cases ***
Login With Valid Credentials
    Open Login Page
    Enter Login Details
    Click Login
    Verify User Is Logged In