from itertools import combinations

def Iterables_and_Iterators_probability(letters, k, target_letter):
    tuples = list(combinations(letters, k))
    contains = [word for word in tuples if target_letter in word]
    probability = len(contains) / len(tuples)
    return probability
    
