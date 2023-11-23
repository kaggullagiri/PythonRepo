from collections import Counter

def word_count(input_list):
    counts = Counter(input_list)
    return len(counts), list(counts.values())
    
