*** Settings ***
Documentation     A test suite containing tests related to invalid login.
...
...               These tests will try out various combinations of invalid login
...               credentials. They use a single keyword, specified with Test Template 
...               setting, that is called with different arguments to cover each
...               of the different combinations.

Suite Setup       Open Browser At Login Page
Suite Teardown    Close Browser
Test Setup        Go To Login Page
Test Template     Login With Invalid Credentials Should Fail
Resource          resource.robot

*** Test Cases ***                                  USERNAME         PASSWORD
No Username Provided                                ${EMPTY}         ${VALID PASSWORD}
No Password Provided                                ${VALID USER}    ${EMPTY}
Neither Username Nor Password Provided              ${EMPTY}         ${EMPTY}
Invalid Username Provided                           invalid_user     ${VALID PASSWORD}
Invalid Password Provided                           ${VALID USER}    invalid_password
Invalid Username And Invalid Password Provided      invalid_user     invalid_password

*** Keywords ***
Login With Invalid Credentials Should Fail
    [Arguments]    ${username}    ${password}
    Input Username And Password    ${username}    ${password}
    Submit Credentials
    Error Page Should Be Open
