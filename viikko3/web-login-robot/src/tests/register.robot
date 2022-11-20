*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  sohvi
    Set Password  sohvi123
    Set Password Confirmation  sohvi123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  s
    Set Password  sohvi123
    Set Password Confirmation  sohvi123
    Submit Credentials
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  sohvi
    Set Password  sohvi12
    Set Password Confirmation  sohvi12
    Submit Credentials
    Register Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Set Username  sohvi
    Set Password  sohvi123
    Set Password Confirmation  sohvi321
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

Login After Successful Registration
    Go To Login Page
    Set Username  sohvi
    Set Password  sohvi123
    Submit Credentials 2
    Login Should Succeed


Login After Failed Registration
    Go To Login Page
    Set Username  s
    Set Password  sohvi123
    Submit Credentials 2
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register

Submit Credentials 2
    Click Button  Login

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}