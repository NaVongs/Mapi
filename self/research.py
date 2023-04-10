import json

cube_amount = []
characters = {}
cubes = {}
cube_ups = {}


file_path = './data.json'
with open(file_path, 'r') as file:
    cube_json = json.load(file)

print(len(cube_json))

def research():
    logs = []
    for log in cube_json:
        cube_amount.append(len(log))
        logs = logs + log
    
    for log in logs:
        name = log['character_name']
        try:
            characters[name] = characters[name] + 1
        except:
            characters[name] = 1
            
        cube = log['cube_type']
        try:
            cubes[cube] = cubes[cube] + 1
        except:
            cubes[cube] = 1
            cube_ups[cube] = 0
    
    for log in logs:
        up = log['item_upgrade_result']
        cube = log['cube_type']
        if up == '성공':
            cube_ups[cube] = cube_ups[cube] + 1

    
    
    return logs
    
        
cube_total_log = research()

print(cube_amount)
print(characters)
print(cubes)
print(cube_ups)