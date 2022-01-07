*** Settings ***
Library    Dialogs
Library    Process


*** Keywords ***
One Argument With Default Value
    [Arguments]    ${arg}=default value
    [Documentation]    This keyword takes 0-1 arguments
    Log    Got argument ${arg}

Two Arguments With Defaults
    [Arguments]    ${arg1}=default 1    ${arg2}=${VARIABLE}
    [Documentation]    This keyword takes 0-2 arguments
    Log    1st argument ${arg1}
    Log    2nd argument ${arg2}

One Required And One With Default
    [Arguments]    ${required}    ${optional}=default
    [Documentation]    This keyword takes 1-2 arguments
    Log    Required: ${required}
    Log    Optional: ${optional}

 Default Based On Earlier Argument
    [Arguments]    ${a}    ${b}=${a}    ${c}=${a} and ${b}
    Should Be Equal    ${a}    ${b}
    Should Be Equal    ${c}    ${a} and ${b}

With Varargs
    [Arguments]    @{varargs}    ${named}
    Log Many    @{varargs}    ${named}

Without Varargs
    [Arguments]    @{}    ${first}    ${second}
    Log Many    ${first}    ${second}

With Positional
    [Arguments]    ${positional}    @{}    ${named}
    Log Many    ${positional}    ${named}

With Free Named
    [Arguments]    @{varargs}    ${named only}    &{free named}
    Log Many    @{varargs}    ${named only}    &{free named}

Return One Value
    Do So

*** Test Cases ***
Example
    With Varargs    named=value
    With Varargs    positional    second positional    named=foobar
    Without Varargs    first=1    second=2
    Without Varargs    second=toka    first=eka
    With Positional    foo    named=bar
    With Positional    named=2    positional=1
    With Free Named    positional    named only=value    x=1    y=2
    With Free Named    foo=a    bar=b    named only=c    quux=d
    And  Default Based On Earlier Argument