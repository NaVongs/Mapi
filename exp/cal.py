import json
# import datetime

file_path = './exp.json'
with open(file_path, 'r') as file:
    exp = json.load(file)
mon_path = "./monpa.json"
with open(mon_path, 'r') as f:
    monpa = json.load(f)

exp_aug ={
    "coup" : 200,
    "boo" : 50,
    "sim" : 25,
    "pend" : 30,
    "small" : 10,
    "gold" : 10,
    "ring" : 10 * 0,
    "union" : 35,
    "hyper" : 10,
    "burn" : 80,
    "vip" : 15,
}

aug_total = sum(exp_aug.values()) / 100
print(aug_total)
mob = 480000
num30 = 6000
print(mob * aug_total * num30)
print(mob * (aug_total+1) * num30 * 3/20)
print(exp["234"] * 0.27 - 250000000*15)

    

def level_cal(curr_lvl, curr_exp_per, burn, target_lvl):
    # curr_lvl = 254
    # burn = False
    # curr_exp_per = 0.06836
        
    curr_exp = int(exp[str(curr_lvl)] * curr_exp_per)

    cnt = 0
    while curr_lvl < target_lvl:
        cnt += 1
        target = int(curr_lvl/5) * 5
        r = 1
        if cnt%7 == 6:
            r = 1.5 
            
        curr_exp += int(r*monpa[str(target)])
        if curr_exp > exp[str(curr_lvl)]:
            curr_exp -= exp[str(curr_lvl)]
            curr_lvl += 1
            if(burn):
                curr_lvl += 2
                if(curr_lvl > 260):
                    curr_lvl = 260
        # print(f"{curr_exp/exp[str(curr_lvl)]}")
        
    print(cnt)
    
    
level_cal(254, 0.06836, False, 258)
level_cal(234, 0,True, 260)