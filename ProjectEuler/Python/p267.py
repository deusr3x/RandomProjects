import numpy as np
ans = []

for i in range(10000):
    f = 0.1+4*i/100000.
    logf = np.log(1+f)
    lognf = np.log(1-f)
    for j in range(1000):
        if j*logf + (1000 - j)*lognf >= np.log(1000000000):
            ans.append(j)
            break            

answ = np.min(ans)
print(answ)




accum = 1
for i in range(1,1000-answ):
    accum *= (1001 - (i))
    accum /= i
answer = accum/(2.0**1000)
print(answer)