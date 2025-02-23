# Scalar Multiplication of a Matrix
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	result=[[scalar*j for j in i]for i in matrix]
	return result