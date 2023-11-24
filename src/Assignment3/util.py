def second_highest(values):
    rduplicate = list(set(values)) # here removing the duplicates
    rduplicate.sort()
    return rduplicate[-2]
    
