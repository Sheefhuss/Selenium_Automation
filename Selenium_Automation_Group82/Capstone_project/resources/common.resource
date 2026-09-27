*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem

*** Variables ***
${URL}              https://automationexercise.com
${BROWSER}          chrome
${USER_EMAIL}       sheefa_hss_test_12345@gmail.com
${USER_PASSWORD}    Password123
${USER_NAME}        Sheefa

# Flag file: created once registration succeeds. While it exists,
# registration and login are skipped on every later run.
${FLAG_FILE}        ${EXECDIR}${/}registration_done.flag

*** Keywords ***
Open Application
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Screenshot Directory    ${OUTPUT DIR}${/}screenshots

Close Application
    Close All Browsers

Registration Already Done
    ${done}=    Run Keyword And Return Status    File Should Exist    ${FLAG_FILE}
    RETURN    ${done}

Mark Registration Done
    Create File    ${FLAG_FILE}    registered

Take Test Screenshot
    [Documentation]    Saves one screenshot per test, named after the test and its status.
    IF    '${TEST STATUS}' != 'SKIP'
        Capture Page Screenshot    ${SUITE NAME}_${TEST NAME}_${TEST STATUS}.png
    END
