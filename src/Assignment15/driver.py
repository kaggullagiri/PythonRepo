import numpy as np
from src.Assignment15.util import mean_var_std_stats

if __name__ == "__main__":
    N, M = map(int, input().split())
    A = np.array([list(map(int, input().split())) for i in range(N)])

    mean_result, var_result, std_result = mean_var_std_stats(A)

    print(mean_result)
    print(var_result)
    print(std_result)
    
