*** Settings ***
Documentation        Test HTTPS Access of an FQDN and query in DNS
...                  new line of doc :D
...    
Library    RequestsLibrary
Library    CustomLibrary.py

*** Variables ***
${fqdn}=     credit-suisse.com


*** Test Cases ***
Query FQDN
    [Documentation]    lookup A record of ${fqdn}
    [Tags]    dns
    ${resp}=    Query
    Should Be Equal     185.27.184.155     ${resp}

GET HTTPS FQDN
    [Documentation]     Make a https get request to ${fqdn}
    [Tags]    http
    GET       https://${fqdn}
    Status Should Be     200



*** Keywords ***
Query
    ${value}=    nsquery    ${fqdn}
    RETURN       ${value}


