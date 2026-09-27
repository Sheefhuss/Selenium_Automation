*** Settings ***
Resource    ../resources/common.resource
Resource    ../resources/product_page.resource

Suite Setup       Open Application
Suite Teardown    Close Application
Test Teardown     Take Test Screenshot

*** Test Cases ***
Search For Product
    Open Products Page
    Search Product    Blue Top
    Verify Product Is Displayed    Blue Top