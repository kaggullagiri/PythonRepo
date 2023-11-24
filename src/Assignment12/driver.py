from src.Assignment12.util import max_of_min
import numpy as np

if __name__ == "__main__":
    N, M = map(int, input().split())
    storage = np.array([input().split() for i in range(N)], int)

    result = max_of_min(storage)

    print(result)
    
    
