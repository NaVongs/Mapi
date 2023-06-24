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
        if(log['potential_option_grade'] == "레어" and log['item_upgrade_result'] == "실패"):
            continue
        if(log['item_equip_part'] == "무기" or log['item_equip_part'] == "보조무기" or log['item_equip_part'] == "엠블렘"):
            continue
        
        if name not in names:
            names[name] = {}
        items_ = names[name]
        if cube not in items_:
            items_[cube] = [[{}, {}, {}], [{}, {}, {}], 0]
        item_cube__ = items_[cube]
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
                
        
        
        
    return logs
    
        
cube_total_log = research()


# print(names)

bar = '----------------------------------------------------------------------------------------------------' 

write_path = './research_epic.json'
with open(write_path, 'w') as output:
    json.dump(names, output, indent=4, ensure_ascii=False)