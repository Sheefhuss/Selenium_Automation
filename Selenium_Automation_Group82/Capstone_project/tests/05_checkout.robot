*** Settings ***
Resource    ../resources/common.resource
Resource    ../resources/product_page.resource
Resource    ../resources/cart_page.resource

Suite Setup       Open Application
Suite Teardown    Close Application
Test Teardown     Take Test Screenshot

*** Test Cases ***
Proceed To Checkout
    Open Products Page
    Add First Product To Cart
    Open Cart
    Verify Cart Is Displayed
    Proceed To Checkout