#!/usr/bin/env python3

import sys
import json


v_file_path = sys.argv[1].strip()
page_embedding_file_path = sys.argv[2].strip()

pagerank = {}
data = None

def dot(v1,v2):
	return sum(x*y for x,y in zip(v1,v2))

def norm(v):
	s = sum(i*i for i in v)
	return s**0.5
	
def similarity(p,q):
	return (dot(p,q))/(norm(p)*norm(q))


with open(v_file_path) as v, open(page_embedding_file_path) as p_embed:

	data = json.load(p_embed)
	
	lines = v.read().strip().split('\n')

	for line in lines:
		try:
			page,rank = line.split(',')
			page,rank = page.strip(),float(rank.strip())
		except:
			continue
		
		pagerank[page] = rank
		
for inp in sys.stdin:
	inp = inp.strip()
	try:
		
		from_node,to_nodes = inp.split('\t')
		from_node,to_nodes = from_node.strip(),eval(to_nodes.strip())
		
	except:
		continue

	initial_contribution = (pagerank[from_node])/(len(to_nodes))
	print(f"{from_node},0")
	for node in to_nodes:
		contribution = initial_contribution * similarity(data[node],data[from_node])
		print(f"{node},{contribution}")

			
	
	 		
	


