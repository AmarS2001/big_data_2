#!/usr/bin/env python3

import sys

c_node = None
n_page=None

pg_rank= 0.15

for line in sys.stdin:
    try:
        s_node,contrib = line.split(',')
        s_node = s_node.strip()
        contrib = float(contrib.strip())
        
    except:
        continue

    if c_node == n_page:
        c_node = s_node
        pg_rank = 0.15+0.85 * contrib

    elif c_node == s_node:
        pg_rank += 0.85 * contrib

    else:
        print("{}, {:.2f}".format(c_node, pg_rank))
        c_node = s_node
        pg_rank = 0.15+0.85 * contrib

print("{}, {:.2f}".format(c_node, pg_rank))
