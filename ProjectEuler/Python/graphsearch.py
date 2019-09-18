from collections import namedtuple
from pprint import pprint as pp
import csv

inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')

class Graph():
	def __init__(self, edges):
		self.edges = edges2 = [Edge(*edge) for edge in edges]
		self.vertices = set(sum(([e.start, e.end] for e in edges2), []))

	def dijkstra(self, source, dest):
		assert source in self.vertices
		dist = {vertex: inf for vertex in self.vertices}
		# print dist
		previous = {vertex: None for vertex in self.vertices}
		dist[source] = 0
		# print "1",dist
		q = self.vertices.copy()
		neighbours = {vertex: set() for vertex in self.vertices}
		# print "1.1",neighbours
		for start, end, cost in self.edges:
			# print 'start',start,'end',end,'cost',cost
			neighbours[start].add((end, cost))
		# pp(neighbours)
		# print "2",q
		while q:
			# print dist
			u = min(q, key=lambda vertex: dist[vertex])
			# print "here ",q, u
			q.remove(u)
			if dist[u] == inf or u == dest:
				break
			for v, cost in neighbours[u]:
				# print v, cost, dist[u],dist[v]
				alt = dist[u] + cost
				# print alt
				if alt < dist[v]:                                  # Relax (u,v,a)
					dist[v] = alt
					previous[v] = u
				# print v, cost, dist[u],dist[v]
		# pp(previous)
		s, u = [], dest
		while previous[u]:
			s.insert(0, u)
			u = previous[u]
		s.insert(0, u)
		return s

mymap = []
mapkey = {}
with open('mygrid4.csv','rb') as csvfile:
	f = csv.reader(csvfile,delimiter=',')
	f.next()
	for row in f:
		mymap.append((row[0],row[1],int(row[2])))
		mapkey[row[0]+';'+row[1]] = int(row[2])
		
	
graph = Graph(mymap)
s = graph.dijkstra("0", "6401")
a=0
for i in range(len(s)-1):
	print(s[i],s[i+1],mapkey[s[i]+';'+s[i+1]])
	a+=mapkey[s[i]+';'+s[i+1]]
print(a)