import numpy as np
import csv
count = 0
x=0.
y=0.
with open('p102_triangles.csv','r') as csvfile:
	f = csv.reader(csvfile,delimiter=',')
	# f.next()
	next(f)
	for row in f:
		a = [int(row[0]) , int(row[1])]
		b = [int(row[2]) , int(row[3])]
		c = [int(row[4]) , int(row[5])]
		denom = float((b[1]-c[1])*(a[0]-c[0])+(c[0]-b[0])*(a[1]-c[1]))
		aa = ((b[1]-c[1])*(x-c[0])+(c[0]-b[0])*(y-c[1]))/denom
		bb = ((c[1]-a[1])*(x-c[0])+(a[0]-c[0])*(y-c[1]))/denom
		cc = 1-aa-bb
		if 0<=aa and aa<=1 and 0<=bb and bb<=1 and 0<=cc and cc<=1:
			count+=1
print(count)