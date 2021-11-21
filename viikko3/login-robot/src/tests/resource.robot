*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input Login Command
    Input  login

Input Credentials
    [Arguments]  ${username}  ${password}
    Input  ${username}
    Input  ${password}
    Run Application

Check Credentials
    [Arguments]  ${username}  ${password}
    Input  ${username}
    Input  ${password}
    Check Credentials  ${username}
    Check Credentials  ${password}

Input New Command
    Input  new
