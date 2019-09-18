import fractions
denprod = 1
numprod = 1
for i in range(1,11):
	for j in range(1,i+1):
		for k in range(1,j+1):
			if (k*10+i)*j == k*(i*10 + j):
				denprod *= j
				numprod *= k

denprod /= fractions.gcd(numprod,denprod)

print denprod