*** Settings ***


*** Test Cases ***
ShowMyList
    ${lists} =    Create List    first    second    third
    FOR    ${element}    IN    @{lists}
        Start Element    ${element}
    END


*** Keywords ***
Return One Value
    [Arguments]    ${arg}

