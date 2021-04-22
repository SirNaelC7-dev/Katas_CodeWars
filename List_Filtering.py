def filter_list(l):
	lt = []
	for x in l:
		if type(x) != str:
			lt.append(x)
	return lt