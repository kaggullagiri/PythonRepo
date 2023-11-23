import numpy as np


def round_array(input_array):
    array = np.array(input_array, float)
    floor_result = np.floor(array)
    ceil_result = np.ceil(array)
    rint_result = np.rint(array)

    return floor_result, ceil_result, rint_result