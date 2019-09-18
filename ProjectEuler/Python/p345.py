import numpy as np

ans = []
with open('p345_matrix.txt','r') as f:
	for row in f:
		ans.append([int(i) for i in row.split(' ')])
		print(ans)
s = 0
for i in ans:
	s+=max(i)
print(s)