# Reshape Matrix
import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	if new_shape[0]*new_shape[1]!=len(a)*len(a[0]):
		return None
	mat=[]
	for i in a:
		for j in i:
			mat.append(j)	
	reshaped_matrix=[]
	s=0
	for i in range(new_shape[0]):
		ele=mat[s:s+new_shape[1]]
		reshaped_matrix.append(ele)
		s+=new_shape[1]
		# or
		# using numpy's reshape function
		x=np.reshape(a,new_shape)
	reshaped_matrix=x.tolist()
	return reshaped_matrix