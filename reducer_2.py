#!/usr/bin/env python3

import sys
def rank(p):
	return 0.15 + 0.85 * p

prev_page = None
#prev_page_rank = 0.15

for line in sys.stdin:
	try:
		from_page,contribution = line.split(',')
		from_page,contribution = from_page.strip(),float(contribution.strip())
		
	except:
		continue
	
	if prev_page == None:
		prev_page = from_page
		prev_page_rank = rank(contribution)
	
	elif prev_page == from_page:
		prev_page_rank += 0.85 * contribution
		
	else:
		print("{},{:.2f}".format(prev_page,prev_page_rank))
		prev_page = from_page
		prev_page_rank = rank(contribution)
		
print("{},{:.2f}".format(prev_page,prev_page_rank))
