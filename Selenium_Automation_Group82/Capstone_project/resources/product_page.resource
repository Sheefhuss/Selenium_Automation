*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${PRODUCTS_LINK}       xpath=//a[contains(text(),'Products')]
${SEARCH_BOX}          id=search_product
${SEARCH_BUTTON}       id=submit_search
${ADD_TO_CART}         xpath=(//a[contains(@class,'add-to-cart')])[1]
${CART_LINK}           xpath=//a[@href='/view_cart']

*** Keywords ***
Open Products Page
    Execute Javascript    window.location.href='/products'
    Wait Until Element Is Visible    ${SEARCH_BOX}    15s

Search Product
    [Arguments]    ${product}
    Input Text    ${SEARCH_BOX}    ${product}
    Scroll Element Into View    ${SEARCH_BUTTON}
    Execute Javascript    document.querySelector("#submit_search").click()

Verify Product Is Displayed
    [Arguments]    ${product}
    Page Should Contain    ${product}

Add First Product To Cart
    Scroll Element Into View    ${ADD_TO_CART}
    Execute Javascript    document.querySelector("a[data-product-id='1']").click()
    Sleep    2s

Open Cart
    Execute Javascript    window.location.href='/view_cart'
    Wait Until Page Contains    Shopping Cart    15s