def score_of_happiness(elements, set_A, set_B):
    return sum(1 if element in set_A else -1 if element in set_B else 0 for element in elements)
    
