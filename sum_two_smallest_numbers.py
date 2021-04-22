def sum_two_smallest_numbers(numbers):
    s = 0
    for x in range(2):
	    s+=min(numbers)
	    numbers.remove(min(numbers))
    return s
