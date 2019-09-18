import collections
cubes = []
c = {}
f = {}
for i in range(1,10000):
	# cubes.append(i**3)
	b = [int(j) for j in str(i**3)]
	b.sort()
	d = ''.join([str(j) for j in b])
	l = len(b)
	if c.get(l,0)==0:
		c[l] = []
	c[l].append(str(b))
	if f.get(d,0)==0:
		f[d] = []
	f[d].append(i**3)


# maxx = 0
# while maxx != 5:
	# for i in c:
		# a = collections.Counter(c[i])
		# for j in a:
			# if a[j] ==5:
				# maxx=5
				# key = 
		
# print f['012334556789']