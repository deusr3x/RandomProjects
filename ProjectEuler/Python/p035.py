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
count = set()
for i in primeset:
	stri = [int(j) for j in str(i)]
	tracker=0
	for k in range(1,len(stri)):
		h = np.roll(stri,k)
		num = int(''.join(str(l) for l in h))
		if num in primeset:
			tracker+=1
	if tracker==len(stri)-1:
		count.add(i)
print len(count)