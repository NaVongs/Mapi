import json
lvl = {}
lvl[230] = 83667084404
for i in range(231, 260):
    if(i%5 == 0):
        if(i == 250):
            lvl[i] = int(lvl[i-1]*1.5)
            if lvl[i] != 442457484960:
                print("warning")
                print(lvl[i])
        elif(i == 255):
            lvl[i] = int(lvl[i-1]*1.03)
        else:
            lvl[i] = int(lvl[i-1]*1.3)
    else:
        lvl[i] = int(lvl[i-1]*1.03)
 
lvl[260] = 10882478440008
        
        
print(lvl)
file_path = "./exp.json"
with open(file_path, 'w') as f:
    json.dump(lvl, f, indent=4)