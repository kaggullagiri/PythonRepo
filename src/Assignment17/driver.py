from src.Assignment17.util import word_count

if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))
    input_list = [input().strip() for i in range(n)]

    unique_count, occurrences = word_count(input_list)

    print("Number of unique elements:", unique_count)
    print("Occurrences:", *occurrences)
    
