*** Settings ***
Documentation     A test suite with which tests for valid login scenario.
...
...               There is only a single valid login scenario in this demo,
...               the credentials for which are defined in the imported
...               resource file.

Resource          resource.robot

*** Test Cases ***
Login With Valid Credentials Should Pass
    [Setup]    Open Browser To Login Page
    Input Username And Password   ${VALID USER}   ${VALID PASSWORD}
    Submit Credentials
    Welcome Page Should Be Open
    [Teardown]    Close Browser
