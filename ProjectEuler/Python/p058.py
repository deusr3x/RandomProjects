import numpy as np
def isprime(n):
	'''check if integer n is a prime'''
	# make sure n is a positive integer
	n = abs(int(n))
	# 0 and 1 are not primes
	if n < 2:
		return False
	# 2 is the only even prime number
	if n == 2: 
		return True    
	# all other even numbers are not primes
	if not n & 1: 
		return False
	# range starts with 3 and only needs to go up the squareroot of n
	# for all odd numbers
	for x in range(3, int(n**0.5)+1, 2):
		if n % x == 0:
			return False
	return True
	
# def primesfrom2to(n):
    # """ Input n>=6, Returns a array of primes, 2 <= p < n """
    # sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    # for i in xrange(1,int(n**0.5)/3+1):
        # if sieve[i]:
            # k=3*i+1|1
            # sieve[       k*k/3     ::2*k] = False
            # sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    # return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]

primecount=0
allcount=0
i = 1
while True:
	ne=(2*i + 1)**2
	nw=(2*i + 1)**2-2*i
	sw=(2*i + 1)**2-4*i
	se=(2*i + 1)**2-6*i
	if isprime(ne):
		primecount+=1
	if isprime(nw):
		primecount+=1
	if isprime(sw):
		primecount+=1
	if isprime(se):
		primecount+=1
	allcount+=4
	
	if float(primecount)/float(allcount) <0.1:
		print 2*i-1
		break
	i+=1