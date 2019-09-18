import csv

data = []
c=0
with open('p083_matrix.txt','rb') as f: 
	for row in f:
		for i in row.split(','):
			data.append(int(i))

c = len(row.split(','))
l = len(data)
ans = []
ans.append([0,1,data[0]])
for i in range(1,l-c):
	if (i+1+c)%c != 1:
		ans.append([i,i+1,data[i]])
		# ans.append([i,i-1,data[i-2]])
	if i%c!=1:
		ans.append([i,i-1,data[i-2]])
	# if i%c == 0:
		# ans.append([i,l+1,0])
	if i>c:
		ans.append([i,i-c,data[i-c-1]])
		
	ans.append([i,i+c,data[i+c-1]])
	
ans.append([l-c,l,data[l-c-1]])
for i in range(1,c):
	ans.append([l-c+i,l-c+1+i,data[l-c+i]])
ans.append([l,l+1,0])

with open('mygrid4.csv','wb') as f:
	f.write('Node,Link,Value\n')
	for row in ans:
		f.write(str(row[0])+','+str(row[1])+','+str(row[2])+'\n')
		
# then graphsearch.py