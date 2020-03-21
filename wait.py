import random 
import time
lift1_pos = random.randrange(10)
lift2_pos = random.randrange(10)
avg_wait_list = []

def Average(avg_wait_list): 
    return sum(avg_wait_list) / len(avg_wait_list) 

#Elevator times
for x in range(1001):
    #Calculates distance from Elevators
    u_pos = random.randrange(10)
    d1_u_pos = lift1_pos - u_pos
    d2_u_pos = lift2_pos - u_pos
    if d1_u_pos < d2_u_pos: 
        a_d1_u_pos = abs(d1_u_pos)
        wait = abs(a_d1_u_pos*2+5)
        print(wait, 'seconds')
        lift1_pos = u_pos
        avg_wait_list.append(wait)
    elif d2_u_pos < d1_u_pos:
        a_d2_u_pos = abs(d2_u_pos)
        wait = abs(d2_u_pos*2+5)
        lift2_pos = u_pos
        avg_wait_list.append(wait)
    elif d2_u_pos == d1_u_pos:
        a_d2_u_pos = abs(d2_u_pos)
        wait = abs(d2_u_pos*2+5)
        d2_u_pos = u_pos
        avg_wait_list.append(wait)
print(avg_wait_list)
avg_wait = Average(avg_wait_list)
print(avg_wait, "seconds. Is your average wait.")