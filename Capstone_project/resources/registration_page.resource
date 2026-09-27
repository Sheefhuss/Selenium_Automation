*** Settings ***
Library    SeleniumLibrary
Resource   common.resource

*** Variables ***
${SIGNUP_LOGIN}       xpath=//a[contains(text(),'Signup / Login')]

${NAME}               xpath=//input[@data-qa='signup-name']
${EMAIL}              xpath=//input[@data-qa='signup-email']
${SIGNUP_BUTTON}      xpath=//button[@data-qa='signup-button']

${PASSWORD}           id=password
${FIRST_NAME}         id=first_name
${LAST_NAME}          id=last_name
${ADDRESS}             id=address1
${STATE}              id=state
${CITY}               id=city
${ZIPCODE}             id=zipcode
${MOBILE}             id=mobile_number

${CREATE_BUTTON}      xpath=//button[@data-qa='create-account']

*** Keywords ***
Open Signup Page
    Wait Until Element Is Visible    ${SIGNUP_LOGIN}    15s
    Execute Javascript    document.querySelector("a[href='/login']").click()
    Wait Until Element Is Visible    ${NAME}    10s

Enter Signup Details
    Input Text    ${NAME}    ${USER_NAME}
    Input Text    ${EMAIL}    ${USER_EMAIL}
    Click Button    ${SIGNUP_BUTTON}
    Wait Until Element Is Visible    ${PASSWORD}    10s

Fill Account Information
    Input Text    ${PASSWORD}    ${USER_PASSWORD}
    Input Text    ${FIRST_NAME}    Sheefa
    Input Text    ${LAST_NAME}    Test
    Input Text    ${ADDRESS}    Kolkata
    Input Text    ${STATE}    West Bengal
    Input Text    ${CITY}    Kolkata
    Input Text    ${ZIPCODE}    700001
    Input Text    ${MOBILE}    9876543210

Create Account
    Click Button    ${CREATE_BUTTON}
    Wait Until Location Contains    account_created    15s

Verify Account Created
    Location Should Contain    account_created