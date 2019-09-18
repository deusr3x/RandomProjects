import numpy as np

def factor2finder(num):
	ans = []
	ans.append(0)
	y = 0
	while y <= num:
		for i in range(1,26):
			if y%(2**i)!=0:
				ans.append(i-1)
				break
		y+=1
	return ans
def factor5finder(num):
	ans = []
	ans.append(0)
	y = 0
	while y <= num:
		for i in range(1,11):
			if y%(5**i)!=0:
				ans.append(i-1)
				break
		y+=1
	return ans

twolist = factor2finder(200000)
fivelist = factor5finder(200000)
print len(twolist), len(fivelist)

ntwo = sum(twolist)
nfive = sum(fivelist)
nptwolist = np.asarray(twolist)
npfivelist = np.asarray(fivelist)
print len(nptwolist), len(npfivelist)
print twolist[:10]
cstwolist = np.cumsum(nptwolist)
csfivelist = np.cumsum(npfivelist)
print len(cstwolist), len(csfivelist)
s=0
# for i in range(200000):
	# if i%1000==0:
		# print i
	# for j in range(200000-i):
		# k = 200000 - i - j-1
		# if (ntwo - twolist[i] - twolist[j] - twolist[k] >= 12) and (nfive - fivelist[i] - fivelist[j] - fivelist[k] >=12):
			# s+=1
			
# print s
		