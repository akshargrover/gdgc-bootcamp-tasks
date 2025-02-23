# Transpose of a Matrix
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	b=[]
	for i in range(len(a[0])):
		for j in range(len(a)):
			b.append(a[j][i])
	return b