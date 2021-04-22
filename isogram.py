def is_isogram(string):
    string = string.lower()
    cont = None
    
    if string == '':
    	cont = True

    while True:
    	for x in string[:]:
    		m = string.find(x)
    		if m == 1:
	    		cont = True
	    	elif m != 1:
	    		cont = False
	    	else:
	    		for y in string[:]:
			    	n = string.find(y)
			    	if n >= 2:
			    		cont = False
			    	else:
			    		break

	return cont 