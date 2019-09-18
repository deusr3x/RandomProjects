# import fractions
import numpy as np

# def phi(n):
	# amount = 0

	# for k in range(1, n + 1):
		# if fractions.gcd(n, k) == 1:
			# amount += 1

	# return amount
	
# print phi(6)
# s = 0
# for i in range(1,1000001):
	# g = float(i/phi(i))
	# if g>s:
		# s = g
		# ans = i
# print g, ans
def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    for i in xrange(1,int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0][1:]+1)|1)]
primes = primesfrom2to(200)
limit = 1000000
i = 0
result = 1
while result*primes[i] < limit:
	result *= primes[i]
	i+=1

print result