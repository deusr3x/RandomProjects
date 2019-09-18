nn = 100000
T = set([0.5*i*(i+1) for i in range(1,nn+1)])
P = set([0.5*i*(3*i-1) for i in range(1,nn+1)])
H = set([i*(2*i-1) for i in range(1,nn+1)])
a = set(T).intersection(P)
g = set(a).intersection(H)
print(g)
# def generateTriangles(n):
	# tnums = []
	# for i in range(1,n+1):
		# tnums.append(0.5*i*(i+1))
	# return tnums
# def generatePent(n):
	# tnums = []
	# for i in range(1,n+1):
		# tnums.append(0.5*i*(3*i-1))
	# return tnums
# def generateHex(n):
	# tnums = []
	# for i in range(1,n+1):
		# tnums.append(i*(2*i-1))
	# return tnums
# nn = 100000
# T = generateTriangles(nn)
# T = set(T)
# P = generatePent(nn)
# P = set(P)
# H = generateHex(nn)
# H = set(H)
# a = set(T).intersection(P)
# g = set(a).intersection(H)
# print g

# check = True
# Hex_and_Pen = [[],[]]
# n = 143
# while check:
	# n += 1
	# Hex_and_Pen[0].append(n*(2*n-1))
	# Hex_and_Pen[1].append(n*(3*n-1)/2)
	# if n*(n+1)/2 in Hex_and_Pen[0] and n*(n+1)/2 in Hex_and_Pen[1]:
		# check = False
# print n*(n+1)/2