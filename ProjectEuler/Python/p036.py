
def ispalin(num):
	return str(num)==str(num)[::-1]

num = 0
for i in range(1,1000000):
	if ispalin(i):
		if ispalin(bin(i)[2:]):
			num+=i
			
print num