*** Settings ***
Library    SeleniumLibrary
Resource   common.resource

*** Variables ***
${SIGNUP_LOGIN}      xpath=//a[contains(text(),'Signup / Login')]

${LOGIN_EMAIL}       xpath=//input[@data-qa='login-email']
${LOGIN_PASSWORD}    xpath=//input[@data-qa='login-password']
${LOGIN_BUTTON}      xpath=//button[@data-qa='login-button']

*** Keywords ***
Open Login Page
    Wait Until Element Is Visible    ${SIGNUP_LOGIN}    15s
    Execute Javascript    document.querySelector("a[href='/login']").click()
    Wait Until Element Is Visible    ${LOGIN_EMAIL}    15s

Enter Login Details
    Input Text    ${LOGIN_EMAIL}    ${USER_EMAIL}
    Input Text    ${LOGIN_PASSWORD}    ${USER_PASSWORD}

Click Login
    Click Element    ${LOGIN_BUTTON}

Verify User Is Logged In
    Page Should Contain    Logged in as