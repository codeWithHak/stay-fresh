def count_agent_commands(commands):
    
    # an obj that will hold the key value pairs
    obj = {}
    
    # iterate over commands
    for command in commands:
        
        # split commands and unpack agent_id and agent_commands
        splitted_commands = command.split(':')
        agent_id, agent_command = splitted_commands
        
        agent_id = int(agent_id)
        
        if agent_id not in obj:
           obj[agent_id] = 0
        obj[agent_id] += 1
        
        
    print(obj)
    

# Example usage
commands = [
    "1:move",
    "2:stop",
    "1:turn",
    "3:move",
    "2:move"
]
result = count_agent_commands(commands)
# print(result)  # Expected: {1: 2, 2: 2, 3: 1}