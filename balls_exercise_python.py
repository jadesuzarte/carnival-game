import random

list_of_numbers =[1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5]
colors_and_points = {'yellow': 1, 'red': 2, 'green': 4, 'orange': 5, 'purple': 10}
balls_picked = []
sum_balls =[]
for i in range(1,6):
    x = random.choice(list_of_numbers)
    if x == 1: 
        sum_balls.append(colors_and_points['yellow'])
    elif x == 2: 
       sum_balls.append(colors_and_points["red"])
    elif x == 3:
       sum_balls.append(colors_and_points["green"])
    elif x == 4: 
        sum_balls.append(colors_and_points["orange"])
    else:
       sum_balls.append(colors_and_points["purple"])
    
    balls_picked.append(x)
    
print(balls_picked)
print(sum_balls)
final_points = sum(sum_balls)
print(final_points)

if final_points < 15: 
    print("Go home sir")
elif 15 < final_points < 22 : 
    print("You get a small prize!")
else:
    print("YOU WON THE BIG PRIZE!!!")



    

