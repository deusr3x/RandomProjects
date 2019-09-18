
def reverse(num):
	return int(str(num)[::-1])
def digitsodd(num):
	k = [int(i)%2 for i in str(num)]
	return sum(k) == len(str(num))
count = 0
i = 10
# for i in range(10,1000000001):
while i < 1000:#1000000001:
	a = i + reverse(i)
	if digitsodd(a) and i%10!=0:
		print i,a
		count+=1
	i+=1