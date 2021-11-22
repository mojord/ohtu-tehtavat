*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  lissu
    Set Password  kissu123
    Set Password Confirmation  kissu123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  al
    Set Password  nalle123
    Set Password Confirmation  nalle123
    Submit Credentials
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  nalle
    Set Password  nalle12
    Set Password Confirmation  nalle12
    Submit Credentials
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Nonmatching Password And Password Confirmation
    Set Username  nalle
    Set Password  nalle123
    Set Password Confirmation  nalle122
    Submit Credentials
    Register Should Fail With Message  Password mismatch

Login After Successful Registration
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Submit Logins
    Login Should Succeed

Login After Failed Registration
    Set Username  nalle
    Set Password  nalle123
    Set Password Confirmation  nalle122
    Submit Credentials
    Go To Login Page
    Set Username  nalle
    Set Password  nalle123
    Submit Logins
    Login Should Fail With Message  Invalid username or password



*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Logins
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Text  password_confirmation  ${password_confirmation}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}