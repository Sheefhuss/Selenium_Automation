*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${CHECKOUT_BUTTON}    xpath=//a[contains(@class,'check_out')]

*** Keywords ***
Verify Cart Is Displayed
    Wait Until Page Contains    Shopping Cart    15s

Proceed To Checkout
    Wait Until Element Is Visible    ${CHECKOUT_BUTTON}    15s
    Scroll Element Into View    ${CHECKOUT_BUTTON}
    Click Element    ${CHECKOUT_BUTTON}
    Wait Until Page Contains    Checkout    15s