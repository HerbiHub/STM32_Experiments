#!/usr/bin/env python3.7

import numpy as np
import time

max_num = 1679616
devices = 31
baud_rate = 57600 # 110, 300, 600, 1200, 2400, 4800, 9600, 14400, 19200, 38400, 57600, 115200, 128000 and 256000

ms_per_check = 1 / (baud_rate / 8 / 50 ) + 0.005

print(f"Simulation of {ms_per_check*1000} ms per check")


hidden_nums = tuple()
for i in range(devices):
    hidden_nums = hidden_nums + (np.random.randint(0,max_num+1),)

#hidden_nums = (1,2,3,4,5,6,7,8,9,10)

#hidden_nums = np.linspace(0,1679616,devices)
#hidden_nums = range(devices)
#hidden_nums = tuple(int(x) for x in hidden_nums)

checks = 0

def find_nums(L, U, hidden_nums, D=0):
    time.sleep(ms_per_check)
    m = int(np.ceil((L+U)/2))
    print(f"Loop: L={L:9,} U={U:9,} m={m:9,} d={D}")
    global checks
    checks += 1
    if L == U:
        if L in hidden_nums:
            print(f"Found {L}!")
            return (L,)

        else:
            return None
    ret_list = []

    if not len(list(x for x in hidden_nums if x >= L and x <=U)):
        return []

    #if len(list(x for x in hidden_nums if x >= L and x < m)):
    x = find_nums(L, m-1, hidden_nums, D+1)
    if x is not None:
        ret_list.extend(x)

    #if len(list(x for x in hidden_nums if x >= m and x <= U)):
    x = find_nums(m, U, hidden_nums, D+1)
    if x is not None:
        ret_list.extend(x)

    return ret_list


        

print(hidden_nums)
t0 = time.time()
x = find_nums(0,max_num,hidden_nums)
t1 = time.time()
print(sorted(hidden_nums))
print(sorted(x))
print(f"Checks: {checks:,}")
print(f"Est Time: {checks*ms_per_check:,.3f}")
print(f"{(t1-t0):,.3f} s")


