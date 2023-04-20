def fill(jug_number, water_in_jugs):
    if jug_number == 1:
        water_in_jugs[0] = 3
    if jug_number == 2:
        water_in_jugs[1] = 5
    print(water_in_jugs)
        
def empty(jug_number, water_in_jugs):
    water_in_jugs[jug_number-1] = 0
    print(water_in_jugs)
    
def pour(from_jug, to_jug, water_in_jugs):
    if from_jug == 1:
        if sum(water_in_jugs) <= 5:
            water_in_jugs[1] = sum(water_in_jugs)
            water_in_jugs[0] = 0
        else:
            water_in_jugs[0] = sum(water_in_jugs) - 5
            water_in_jugs[1] = 5
    
    if from_jug == 2:
        if sum(water_in_jugs) <= 3:
            water_in_jugs[0] = sum(water_in_jugs)
            water_in_jugs[1] = 0
        else:
            water_in_jugs[1] = sum(water_in_jugs) - 3
            water_in_jugs[0] = 3
            
    print(water_in_jugs)

if __name__=="__main__":
    
    water_in_jugs = [0]*2
    
    print('Initial Water Level : ',water_in_jugs)
    
    desired_vol = int(input("Enter the number of litres of water you need : "))
    
    while desired_vol <= 5 and desired_vol > 0:
        if desired_vol == water_in_jugs[0] or desired_vol == water_in_jugs[1]:
            break
        if water_in_jugs[1] == 5:
            empty(2,water_in_jugs)
        if water_in_jugs[1] == 5:
            empty(2,water_in_jugs)
        if water_in_jugs[0] == 0:
            fill(1,water_in_jugs)
        pour(1,2,water_in_jugs)
        
    if desired_vol > 5 or desired_vol < 0:
        print('Not Possible')