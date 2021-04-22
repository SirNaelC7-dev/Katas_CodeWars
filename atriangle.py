def is_triangle(a, b, c):
    check = 0
    if abs(a-b) < c < a+b:
    	check+=1
    if abs(a-c) < b < a+c:
    	check+=1
    if abs(b-c) < a < b+c:
    	check+=1
    if check == 3:
    	return True
    else:
    	return False


is_triangle(1,2,2)
#| b - c | < a < b + c
#| a - c | < b < a + c
#| a - b | < c < a + b