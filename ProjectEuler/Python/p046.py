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
def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    for i in xrange(1,int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]

def squaresets(n):
	ans = np.arange(1,n+1)
	return ans**2
primeset = primesfrom2to(10000)
squareset = squaresets(10000)
num = 33
check = True

while check:
	print num
	test = False
	for i in primeset:
		if isprime(num):
			test=True
			break
		# print i
		for j in squareset:
			ans = i+2*j
			# print j
			if num == ans:
				test = True
				# print i,j, num
				break
				
		if test:
			# print test
			break
		# else:
			# print test
			# check = False
			# print num
	if test==False:
		check = False
		print num
	num+=2