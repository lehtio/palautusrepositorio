*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input Login Command
    Input  login

Input Register Command
    Input  register

Input Credentials
    [Arguments]  ${username}  ${password}
    Input  ${username}
    Input  ${password}
    Run Application
