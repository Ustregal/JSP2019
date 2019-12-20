# zad 1 lista 9

import numpy as np
import scipy

A=np.array([[1,2,3,-2,-1],
            [3,5,5,-3,-9],
            [2,3,2,0,-8],
            [2,6,7,-5,1],
            [1,2,6,-4,-10]])

b=np.array([[6],[2],[-5],[17],[12]])
x = np.linalg.solve(A,b)

#print("macierz rozwiazan")
#print("x=\n",x)

print("rozwiazania:")
print("x =", x[0][0])
print("y =", x[1][0])
print("z =", x[2][0])
print("t =", x[3][0])
print("u =", x[4][0])