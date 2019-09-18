import scipy.misc as scm
count = 0
for i in range(1, 101):
	for j in range(1,i):
		if scm.comb(i,j)>1000000:
			count+=1
print count