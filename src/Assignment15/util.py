import numpy as np

def mean_var_std_stats(A):
    mean_result = np.mean(A, axis=1)
    var_result = np.var(A, axis=0)
    std_result = np.round(np.std(A), 11)

    return mean_result, var_result, std_result
    
