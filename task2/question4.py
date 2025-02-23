# Calculate Mean by Row or Column
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode=='column':
		matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
	means=[]
	for i in matrix:
		means.append(sum(i)/len(i))
	return means