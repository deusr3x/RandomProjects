import numpy as np

def factorfinder(num):
	ans=set()
	y = 1
	while y <= np.sqrt(num):
		if num%y==0:
			ans.add(y)
			if int(num/y)!=num:
				ans.add(int(num/y))
		y+=1
	return list(ans)

abundantnums = []
allnums = set()
for i in range(1,28124):
	allnums.add(i)
	a = factorfinder(i)
	if sum(a) > i:
		abundantnums.append(i)

sumnums = set()
for i in abundantnums:
	for j in abundantnums:
		if i+j<=28123:
			sumnums.add(i+j)
		else:
			break
f = allnums.difference(sumnums)
print(sum(list(f)))