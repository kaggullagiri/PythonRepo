from collections import OrderedDict

def split_num_char(string, k):
    i = 0
    while i < len(string):
        word1 = "".join(OrderedDict.fromkeys(string[i: i+k]))
        yield word1
        i = i + k