import numpy as np
def generatePent(n):
	tnums = []
	for i in range(1,n+1):
		tnums.append(0.5*i*(3*i-1))
	return tnums
nn = 5000

P = generatePent(nn)
count = 0
for i in P:
	# print count
	for j in P:
		a = i+j
		b = abs(i-j)
		aa = 3./2.
		bb = -1./2.
		cc = -b
		r1 = (-bb+np.sqrt(bb**2 - 4*aa*cc))/(2*aa)
		r2 = (-bb-np.sqrt(bb**2 - 4*aa*cc))/(2*aa)
		if r1%1==0 or r2%1==0:
			cc=-a
			r3 = (-bb+np.sqrt(bb**2 - 4*aa*cc))/(2*aa)
			r4 = (-bb-np.sqrt(bb**2 - 4*aa*cc))/(2*aa)
			if r3%1==0 or r4%1==0:
				if a in P and b in P:
					print(i,j,b, count)
		# if a in P and b in P:
			# print i, j, b
	count+=1