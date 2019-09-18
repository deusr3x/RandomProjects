
import numpy as np

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(int(n/3) + (n%6==2), dtype=np.bool)
    for i in range(1,int(int(n**0.5)/3)+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       int(k*k/3)     ::int(2*k)] = False
            sieve[int(k*(k-2*(i&1)+4)/3)::int(2*k)] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]
	
primeset = primesfrom2to(1000000)
evens = ['24680']
count=0
a=[]
for i in range(5,len(primeset)):
	stri = str(primeset[i])
	aa = []
	for j in range(1,len(stri)):
		t = stri[j:]
		s = stri[:j]
		if int(t) in primeset and int(s) in primeset:
			aa.append(True)
		else:
			aa.append(False)
			break
	if sum(aa) == len(aa):
		count+=primeset[i]
		a.append(primeset[i])
print(len(a), count)