*** Settings ***
Library  ../AppLibrary.py
Resource  resource.robot

Test Setup  Create User And Input Register Command

*** Test Cases ***
Register With Valid Username And Password
    Input Register Command
    Input Credentials  valid_user  valid_password
    Output Should Contain  User registered successfully



Register With Already Taken Username And Valid Password
    Input Register Command
    Input Credentials  existing_user  valid_password
    Output Should Contain  Username already taken

Register With Too Short Username And Valid Password
    Input Register Command
    Input Credentials  ab  valid_password
    Output Should Contain  Username must be at least 3 characters long

Register With Enough Long But Invalid Username And Valid Password
    Input Register Command
    Input Credentials  invalid_user  valid_password
    Output Should Contain  Invalid characters in username

Register With Valid Username And Too Short Password
    Input Register Command
    Input Credentials  new_user  short
    Output Should Contain  Password must be at least 6 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Register Command
    Input Credentials  another_user  longpassword
    Output Should Contain  User registered successfully

*** Keywords ***
Create User And Input Register Command
    Create User  kalle  kalle123
    Input Register Command