import numpy as np
import math
limit = 1000
result = 0

den = 2
num = 3

for i in range(1,limit+1):
	num+=2*den
	den = num - den
	if int(math.log10(num)) > int(math.log10(den)):
		result+=1
		
print result