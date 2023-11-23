from src.Assignment10.util import calculateaverage

if __name__ == "__main__":
    input_count = int(input("enter input:"))
    fields = input().split()
    data = [input().split() for _ in range(input_count)]

    average = calculateaverage(input_count, fields, data)
    print(f"{average:.2f}")
    
