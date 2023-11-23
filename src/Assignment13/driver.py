import numpy as np
from src.Assignment13.util import Linear_Algebra_determinant

if __name__ == "__main__":
    N = int(input())
    A = np.array([input().split() for _ in range(N)], float)

    result = Linear_Algebra_determinant(A)

    print(result)
    
