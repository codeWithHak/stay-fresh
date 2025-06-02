# Problem: Agent Command Counter

## Description:
You’re building a tool for an agentic AI system to count commands sent by different agents. Given a list of commands (strings) in the format "AgentID:Command", count how many commands each agent sent and return a dictionary with AgentID as keys and command counts as values.

## Constraints:
AgentID is an integer (e.g., 1, 2).
Command is a string (e.g., "move", "stop").
Input format is always valid: "AgentID:Command".
Example:

``` python

commands = [
    "1:move",
    "2:stop",
    "1:turn",
    "3:move",
    "2:move"
]
```
### Output: {1: 2, 2: 2, 3: 1}

## Challenge:
Use a dictionary to count occurrences. Optionally, sort the output dictionary by AgentID for cleaner presentation.