*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  lissu  kissu123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  al  nalle123
    Output Should Contain  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Input Credentials  nalle  nalle12
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  nalle  nillenalle
    Output Should Contain  Password cannot contain only letters

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command
