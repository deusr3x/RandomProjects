
count = 0

for i in range(1,30):
	for j in range(1,100):
		l = len(str(j**i))
		if l == i:
			count +=1
			print i,j, l
print count