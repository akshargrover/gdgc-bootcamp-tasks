# Matrix times Vector
def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
	c=[]
	if a is None or len(a[0]) != len(b):
		return -1
	for i in a:
		pdt=0
		for j in range(len(b)):
			pdt+= i[j]*b[j]
		c.append(pdt)
	return c