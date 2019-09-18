import itertools
def find_all(a_str,sub):
	start = 0
	while True:
		start = a_str.find(sub,start)
		if start == -1: return
		yield start
		start += len(sub)
with open('p059_cipher.txt','rb') as f:
	g = f.read()
	h = g.split(',')

num = 0
m = {}
for i in range(len(h)-3):
	c = h[i:i+3]
	s = ','.join([str(j) for j in c])
	l = len(list(find_all(g,s)))
	m[s] = l
	if l > num:
		num = l
		mystr = s
# r = itertools.combinations('abcdefghijklmnopqrstuvwxyz',3)	
# t = list(r)
# for i in range(500,600):
	# bb = ''.join(chr(c^ord(k)) for c,k in zip([79,59,12],t[i]))
	# print t[i], bb
for i in m:
	if m[i] >8:
		aa = [int(j) for j in i.split(',')]
		# bb = ''.join(chr(c^k) for c,k in itertools.izip([79,59,12,2,79,35],itertools.cycle(aa)))
		print i, m[i]#, bb
		
		
q=''.join(chr(c^ord(k)) for c,k in itertools.izip(d,itertools.cycle(['g','o','d'])))