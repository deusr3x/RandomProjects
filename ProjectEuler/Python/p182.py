import fractions

def getgcd(x,y):
	return fractions.gcd(x,y)
	
p = 1009
q = 3643

n = p*q
phi = (p-1)*(q-1)

ees = []
for i in range(2,phi):
	if getgcd(i,phi)==1:
		ees.append(i)
add={}
loop=0
minnum = 1000000
for k in ees:
	messages = (1+getgcd(k-1,p-1))*(1+getgcd(k-1,q-1))
	add[k] = messages
	if messages<minnum:
		minnum = messages
sol =0 
for i in add:
    if add[i]==minnum:
        sol+=i
print sol
# for k in ees:
	# print loop
	# loop+=1
	# add[k] = 0
	# for i in range(n):
		# if (pow(i,k,n) == i): #(i**k%n == i):
			# add[k]+=1
		# if add[k]>minnum:
			# break
	# if add[k]<minnum:
		# minnum = add[k]