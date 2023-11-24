import numpy as np

def max_of_min(storage):
    return np.max(np.min(storage, axis=1), axis=0)
    
