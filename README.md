# Deterministic Finite Automaton

The algorithm developed verify the validity of a string in an AFD.
As parameters, the function receives the AFD definition - name, final and goal states,
initial state, the transition function and the alphabet sigma.

It works basically reading each character of the given string.
First, we check if the character is present in the alphabet. If yes,
we iterate through the transition functions and check if any of the functions
take us to the next state. Keep doing it until we finish the whole string.

If the last state is a goal state, the function returns `True`, and that string is
valid with the defined AFD. Otherwise, returns `False`, and the string is not valid with
the AFD.

The AFD definition should be in a text file. This file may contain:
- The AFD name
- The number of states
- The initial state
- A line with the goal states, comma separated
- N lines with the transition functions. Each line is defined with a initial state, one input character
and the next state, all separated with a comma. Example: `0,a,1`.

This is a valid AFD definition file:

```text
example_AFD
6
0
ab
2,4
0,a,1
1,b,2
2,a,3
3,a,4
```  