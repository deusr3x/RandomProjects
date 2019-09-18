
def myfunc(num,ans=None):
	if ans is None:
		ans=[num]
	if num == 1 or num==89:
		return ans
	else:
		num = sum([int(i)**2 for i in str(num)])
		ans.append(num)
		myfunc(num,ans)
	return ans
	
def myfunc2(num, storage):
	num = sum([int(i)**2 for i in str(num)])
	if storage[num+1] == 89:
		ans = 1
	else:
		ans=0
	return ans
i = 2
count = 0
storage = []
while i<600:
	ans = myfunc(i)
	storage.append(ans[-1])
	i+=1
print(count)

i = 2
count = 0
while i<10000000:
	if i%1000000==0:
		print(i)
	ans = myfunc2(i,storage)
	count+=ans
	i+=1
print(count) #needs work

# i = 2
# count = 0
# while i<10000000:
	# if i%1000000==0:
		# print i
	# ans = myfunc(i)
	# if ans[-1] == 89:
		# count+=1
	# i+=1
# print count