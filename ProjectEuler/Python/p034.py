import scipy.misc as spm

factorials = {}
for i in range(10):
	factorials[str(i)] = spm.factorial(i)

ans=0
for i in range(3,500000):
	stri=str(i)
	num = 0
	for j in stri:
		# if j == '9' or j =='8':
			# break
		num += factorials[j]
	if num == i:
		print i
		ans+=i
print ans