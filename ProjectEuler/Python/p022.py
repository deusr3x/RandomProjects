
with open('p022_names.txt','rb') as f:
	names = next(f)
	names = names.decode().replace('"','')
	names = names.split(',')
names.sort()
a = {}
f = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
count = 1
for i in f:
	a[i] = count
	count +=1
score = 0
index = 1
for i in names:
	num = 0
	for j in i:
		num+=a[j]
	score+=(num*index)
	index+=1
print(score)