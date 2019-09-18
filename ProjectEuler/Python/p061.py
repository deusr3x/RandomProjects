import itertools
def generateTriangles(n):
	tnums = []
	for i in range(1,n+1):
		tnums.append(0.5*i*(i+1))
	return tnums
def generateSquare(n):
	tnums = []
	for i in range(1,n+1):
		tnums.append(i*i)
	return tnums
def generatePent(n):
	tnums = []
	for i in range(1,n+1):
		tnums.append(0.5*i*(3*i-1))
	return tnums
def generateHex(n):
	tnums = []
	for i in range(1,n+1):
		tnums.append(i*(2*i-1))
	return tnums
def generateHep(n):
	tnums = []
	for i in range(1,n+1):
		tnums.append(i*(5*i-3)/2.)
	return tnums
def generateOct(n):
	tnums = []
	for i in range(1,n+1):
		tnums.append(i*(3*i-2))
	return tnums
	
T = generateTriangles(140)
S = generateSquare(100)
P = generatePent(100)
Hx = generateHex(100)
Hp = generateHep(100)
O = generateOct(100)
rT = []
for i in T:
	if len(str(int(i)))==4:
		rT.append(int(i))
rS = []
for i in S:
	if len(str(int(i)))==4:
		rS.append(int(i))
rP = []
for i in P:
	if len(str(int(i)))==4:
		rP.append(int(i))
rHx = []
for i in Hx:
	if len(str(int(i)))==4:
		rHx.append(int(i))
rHp = []
for i in Hp:
	if len(str(int(i)))==4:
		rHp.append(int(i))
rO = []
for i in O:
	if len(str(int(i)))==4:
		rO.append(int(i))

x = list(itertools.permutations([0,1,2,3,4,5]))
f = [rT,rS,rP,rHx,rHp,rO]
for rs in x:
	for i in f[rs[0]]:
		for j in f[rs[1]]:
			if str(i)[-2:] == str(j)[:2]:
				for k in f[rs[2]]:
					if str(j)[-2:] == str(k)[:2]:
						for l in f[rs[3]]:
							if str(k)[-2:] == str(l)[:2]:
								for ll in f[rs[4]]:
									if str(l)[-2:] == str(ll)[:2]:
										for lll in f[rs[5]]:
											if str(ll)[-2:] == str(lll)[:2] and str(lll)[-2:] == str(i)[:2]:
												print i, j, k, l, ll, lll, i+j+k+l+ll+lll
											# break	