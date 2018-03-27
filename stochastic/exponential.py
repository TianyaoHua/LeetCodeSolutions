import numpy as np
lmd = 0.3
beta = 1/lmd
p = 0.5
N = 1000000
total_time = 0
total_service = 0
delay = []
arrivals = [np.random.exponential(beta) for i in range(N)]
services = [np.random.geometric(p) for i in range(N)]
R = []
for i in range(N):
    total_time += arrivals[i]
    start_time = np.ceil(total_time)
    r = start_time-total_time
    R.append(r)
    if start_time >= total_service:
        delay_ = r + services[i]
        delay.append(delay_)
        total_service = start_time + services[i]
    else:
        delay_ = total_service-total_time + services[i]
        delay.append(delay_)
        total_service += services[i]
# for i in range(N):
#     total_time += arrivals[i]
#     if total_time >= total_service:
#         delay_ = services[i]
#         delay.append(delay_)
#         total_service = total_time + services[i]
#     else:
#         delay_ = total_service-total_time + services[i]
#         delay.append(delay_)
#         total_service += services[i]
print(np.average(delay))
print(np.average(arrivals))
print(np.average(services))
averate_D = (1/p + 1/2-1)/(1-lmd/p)+1

print(averate_D)

print(np.average(R))

