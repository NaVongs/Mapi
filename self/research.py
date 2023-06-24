import json
import re

cube_amount = []
characters = {}
cubes = {}
cube_ups = {}
items = {}
names = {}

file_path = './data.json'
with open(file_path, 'r') as file:
    cube_json = json.load(file)

print(len(cube_json))


# class item_cube_opt():
#     def __init__(self):
#         self.cube_list = {}
                
#     def __str__(self):
#         return f"""{self.cube_list}"""
        
#     def __repr__(self):
#         return f"""upper pot \n
#                 {self.cube_list}"""

    
    


def research():
    logs = []
    for log in cube_json:
        cube_amount.append(len(log))
        logs = logs + log
        
        
    for log in logs:
        item = log['target_item']
        cube = log['cube_type']
        name = log['character_name']
        if(cube != "수상한 큐브"):
            continue
        
        if name not in names:
            names[name] = {}
        items_ = names[name]
        
        if item not in items_:
            items_[item] = {}
        item__ = items_[item]
        if cube not in item__:
            item__[cube] = [[{}, {}, {}], [{}, {}, {}], 0]
        item_cube__ = item__[cube]
        item_cube__[2] += 1
            
        target_pot = 0
        got_opt = log['after_potential_options']
        if len(got_opt) == 0 :
            got_opt = log['after_additional_potential_options']
            target_pot = 1
        for i in range(len(got_opt)):
            opt = got_opt[i]["value"]
            if opt in item_cube__[target_pot][i]:
                item_cube__[target_pot][i][opt] += 1
            else:
                item_cube__[target_pot][i][opt] = 1
                
        
            
        
    
    # for log in logs:
    #     name = log['character_name']
    #     if name in characters:
    #         characters[name] += 1
    #     else :
    #         characters[name] = 1
            
    #     cube = log['cube_type']
    #     if cube in cubes:
    #         cubes[cube] += 1
    #     else:
    #         cubes[cube] = 1
    #         cube_ups[cube] = 0
    
    # for log in logs:
    #     up = log['item_upgrade_result']
    #     cube = log['cube_type']
    #     if up == '성공':
    #         cube_ups[cube] = cube_ups[cube] + 1
        
        
    
    
    return logs
    
        
cube_total_log = research()

# print(cube_amount)
# print(characters)
# print(cubes)
# print(cube_ups)
print(items)

bar = '----------------------------------------------------------------------------------------------------' 

write_path = './research.json'
with open(write_path, 'w') as output:
    json.dump(names, output, indent=4, ensure_ascii=False)