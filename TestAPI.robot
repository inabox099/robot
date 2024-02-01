*** Settings ***
Documentation        Test HTTPS Access of an FQDN and query in DNS
...                  new line of doc :D
...    
Library    RequestsLibrary
Library    Collections
Suite Setup    Create authenticated Session

*** Variables ***
${user}=    username
${passwd}=    password


*** Test Cases ***
GET an existing user, notice how the schema gets more accurate
    ${params}=    Create Dictionary    high=10    low=5
    ${response}=    GET On Session   alias=random     url=http://127.0.0.1:8000/random    params=${params}
    ${is int}=    Evaluate    isinstance(${response.json()['number']}, int)
    Log To Console     ${is int}
    Should Be True     ${is int}

GET without Session
    ${params}=    Create Dictionary    high=10    low=5
    GET     url=http://127.0.0.1:8000/random     params=${params}    expected_status=401
    Status Should Be     401

*** Keywords ***
Create authenticated Session
    ${auth}=    Create List    ${user}    ${passwd}
    Create Session    alias=random    url=http://127.0.0.1:8000/random    auth=${auth}