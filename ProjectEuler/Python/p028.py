

ne = 0
nw = 0
sw = 0
se = 0
for i in range(1,501):
	ne+=(2*i + 1)**2
	nw+=(2*i + 1)**2-2*i
	sw+=(2*i + 1)**2-4*i
	se+=(2*i + 1)**2-6*i
print(ne+nw+sw+se+1)