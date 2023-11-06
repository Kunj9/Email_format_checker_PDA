# PDA (Pushdown Automaton) String Checker
This Python program, a PDA string checker, validates input strings based on a predefined set of rules. The program simulates a Pushdown Automaton (PDA) with states and transitions to determine whether a given string adheres to the specified rules. The PDA is designed to accept strings in a specific format and reject those that do not meet the criteria.

## Program Description
The PDA follows a set of rules for recognizing valid strings. It checks for the presence of specific characters, patterns, and sequences within the input string. If the string adheres to the rules, it is accepted; otherwise, it is rejected.

## PDA States and Transitions
The PDA uses states to keep track of its progress while reading the input string. Each state corresponds to a specific phase of the validation process. The transitions between states are determined by the characters read from the input string and the operations performed on the stack.

### States:
1. **State 1**: Initial state, checks for the presence of `%` at the beginning.
2. **State 2**: Checks for the presence of `(` and digits, with respective actions.
3. **State 3**: Continues checking for digits.
4. **State 4**: Checks for the presence of a dot `.` after digits.
5. **State 5**: Validates operators and digits.
6. **State 6**: Verifies the presence of `)` and `%`.
7. **State 7**: Final state, accepts the string if the stack is empty.

## How to Use
1. Run the program and answer the prompt with 'y' to enter a string for validation.
2. Enter the string you want to check based on the rules outlined in the program.
3. The program will display the sequence of states and actions taken for each character in the string.
4. The string will be accepted if it reaches State 7, and the stack is empty. Otherwise, it will be rejected.

### Example Input and Output:
#### Valid Input:
Enter a string: %((12.34+56)/78)%

#### Output:
PDA's Starting state: q1
In State 1 Read character: % pop ε push % | ( , ε --> % )
In State 2 Read character: ( pop ε push ) | ( , ε --> ) )
In State 3 Read character: 1 pop ε push ε | ( , ε --> ε )
In State 3 Read character: 2 pop ε push ε | ( , ε --> ε )
In State 4 Read character: . pop ε push ε | ( , ε --> ε )
In State 3 Read character: 3 pop ε push ε | ( , ε --> ε )
In State 3 Read character: 4 pop ε push ε | ( , ε --> ε )
In State 5 Read character: + pop ε push ε | ( , ε --> ε )
In State 5 Read character: 5 pop ε push ε | ( , ε --> ε )
In State 2 Read character: / pop ε push / | ( , ε --> / )
In State 3 Read character: 7 pop ε push ε | ( , ε --> ε )
In State 3 Read character: 8 pop ε push ε | ( , ε --> ε )
In State 6 Read character: ) pop ) push ε | ) , ) --> ε )
In State 7 Read character: % pop % push ε | % , % --> ε )
String is accepted

#### Invalid Input:
Enter a string: %(12.+56)%

#### Output:
PDA's Starting state: q1
In State 1 Read character: % pop ε push % | ( , ε --> % )
In State 2 Read character: ( pop ε push ) | ( , ε --> ) )
In State 3 Read character: 1 pop ε push ε | ( , ε --> ε )
In State 2 Read character: . pop ε push ) | . , ε --> ) )
PDA crashes before reaching the end of the input string.
String is rejected

## Disclaimer
This program is designed for educational purposes to demonstrate the functioning of a PDA and its validation process. It does not provide extensive error handling or support for complex input validation. The PDA's rules are predefined and limited to the described states and transitions.
