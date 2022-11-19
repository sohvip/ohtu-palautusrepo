*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  sohvi  sohvi123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  sohvi  sohvi123
    Input New Command
    Input Credentials  sohvi  sohvi123
    Output Should Contain  User with username sohvi already exists

Register With Too Short Username And Valid Password
    Input Credentials  s  sohvi123
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input Credentials  sohvi  sohvi12
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  sohvi  sohvivhos
    Output Should Contain  Password is too simple

*** Keywords ***
Input New Command and Create User
    Input New Command
    Create User  kalle  kalle123
