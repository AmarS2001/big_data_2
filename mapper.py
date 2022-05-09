#!/usr/bin/env python3
import sys
import json
import math

p_rank=dict()
v_path= sys.argv[1]
json_path= sys.argv[2]

def similarity(a, b):
	res = 0
	mod_1 = 0
	mod_2 = 0
	arr_len = len(a)
	i = 0 
	while(i < arr_len):
		res += a[i] * b[i]
		mod_1 += (a[i])**2
		mod_2 += (b[i])**2
		i += 1
	return (   (res) / (  ((mod_1)**0.5) * ((mod_2)**0.5)  )   )

with open(v_path) as v, open(json_path) as j_fil:
    data= json.load(j_fil)
    lines = v.read()
    lines = lines.strip().split('\n')
    for line in lines:
        try:
            page,rank= line.split(',')
            page =page.strip()
            rank =float(rank.strip())
        except:
            continue
        p_rank[page]=rank

for line2 in sys.stdin:
    line2=line2.strip()
    try:
        s_node,t_lis=line2.split('\t')
        s_node= s_node.strip()
        t_lis= eval(t_lis.strip())
    except:
        continue

    try:
        i_cont= (p_rank[s_node])/(len(t_lis))
        print(f"{s_node},0")

        for node in t_lis:
            cont=i_cont* similarity(data[node],data[s_node])
            node=int(node)
            print(f"{node},{cont}")
    except:
        continue



