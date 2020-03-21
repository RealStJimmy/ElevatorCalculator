import random 
import time
lift1_pos = random.randrange(10)
lift2_pos = random.randrange(10)



while True:
    u_pos = input("What floor are you on? 0 - 9? ")
    u_pos = int(u_pos)
    #Calculates distance from Elevators
    d1_u_pos = lift1_pos - u_pos
    d2_u_pos = lift2_pos - u_pos

    if d1_u_pos < d2_u_pos: 
        print(lift1_pos)
        print(d1_u_pos)
        a_d1_u_pos = abs(d1_u_pos)
        wait = abs(a_d1_u_pos*2+5)
        print(wait, 'seconds')
        lift1_pos = u_pos
        time.sleep(wait)
        print("Lift 1 is here")
    elif d2_u_pos < d1_u_pos:
        a_d2_u_pos = abs(d2_u_pos)
        wait = abs(d2_u_pos*2+5)
        print(wait)
        print(lift2_pos)
        lift2_pos = u_pos
        time.sleep(wait)
        print("Lift 2 is here")
    elif d2_u_pos == d1_u_pos:
        a_d2_u_pos = abs(d2_u_pos)
        wait = abs(d2_u_pos*2+5)
        print(wait)
        print(lift2_pos)
        d2_u_pos = u_pos
        time.sleep(wait)
        print("Lift 2 is here")