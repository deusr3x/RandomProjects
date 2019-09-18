import numpy as np

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    for i in xrange(1,int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]

primeset = primesfrom2to(1000000)
reducedset = []
for i in primeset:
	if len(str(i))==4:
		reducedset.append(i)
		
g = {}

for i in reducedset:
	g[i] = []
	pp = [int(k) for k in str(i)]
	pp.sort()
	for j in reducedset:
		p = [int(k) for k in str(j)]
		p.sort()
		if p==pp:
			g[i].append(j)

for k in g:			
	for i in g[k]:
		for j in g[k]:
			x = 2*i - j
			if x in g[k] and i<j:
				print i,j, x