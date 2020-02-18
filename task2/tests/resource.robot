*** Settings ***
Documentation     A resource file with reusable keywords and variables.
...
...               Defines common keywords to be used in testing the login
...               functionality for 'system X'. They are wrappers around keywords
...               provided by the imported SeleniumLibrary.

Library           SeleniumLibrary

*** Variables ***
${BASE ADDRESS}     localhost:1234/system_x
${LOGIN URL}        http://${BASE ADDRESS}/index.html
${WELCOME URL}      http://${BASE ADDRESS}/welcome.html
${ERROR URL}        http://${BASE ADDRESS}/error.html
${BROWSER}          chrome
${VALID USER}       admin
${VALID PASSWORD}   admin

*** Keywords ***
Open Browser At Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Login Page Should Be Open

Go To Login Page
    Go To    ${LOGIN URL}
    Login Page Should Be Open

Login Page Should Be Open
    Title Should Be    Enter Credentials

Input Username And Password
    [Arguments]    ${username}    ${password}
    Input Text    username_field    ${username}
    Input Text    password_field    ${password}

Submit Credentials
    Click Button    login_button

Welcome Page Should Be Open
    Location Should Be    ${WELCOME URL}
    Title Should Be    Login Succeeded

Error Page Should Be Open
    Location Should Be    ${ERROR URL}
    Title Should Be    Login Failed
