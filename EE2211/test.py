import numpy as np
import A1_A028xxxxN as grading

X = np.array([[1, 1], [4, 2], [4, 6], [3, -6], [0, -10]])
y = np.array([[-3], [2], [1], [5], [4]])
InvXTX, w = grading.A1_A028xxxxN(X, y)
print(InvXTX)
print(w)
