def tribonacci(signature, n):
    a, b, c = signature[0], signature[1], signature[2]
    seq = []
    vf = []
    for num in signature:
    	seq.append(num)
    while len(seq) < n:
    	aux = a+b+c
    	seq.append(aux)
    	a, b, c = b, c, aux
    for x in range(0,n):
    	vf.append(seq[x])

    return vf