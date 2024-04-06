t = 1
t_sravn = 0
k = 0
while t != 0:
    t = float(input())
    if t_sravn > t:
        k += 1
        t_sravn = t
print(k)