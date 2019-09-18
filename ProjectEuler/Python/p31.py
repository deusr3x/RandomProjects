cents = 200
denominations = [200, 100, 50, 20, 10, 5, 2, 1]
names = {200: "2Pound(s)", 100: "1Pounds(s)", 50 : "p(s)", 20 : "p",10:"p",5:"p",2:"p",1:"p"}

def count_combs(left, i, comb, add):
	if add: comb.append(add)
	if left == 0 or (i+1) == len(denominations):
		if (i+1) == len(denominations) and left > 0:
			comb.append( (left, denominations[i]) )
			i += 1
		while i < len(denominations):
			comb.append( (0, denominations[i]) )
			i += 1
		# print " ".join("%d %s" % (n,names[c]) for (n,c) in comb)
		return 1
	cur = denominations[i]
	return sum(count_combs(left-x*cur, i+1, comb[:], (x,cur)) for x in range(0, int(left/cur)+1))

print(count_combs(cents, 0, [], None))