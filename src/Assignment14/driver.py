from src.Assignment14.util import score_of_happiness

if __name__ == "__main__":
    n, m = map(int, input().split())
    elements = list(map(int, input().split()))
    set_A, set_B = set(map(int, input().split())), set(map(int, input().split()))

    happiness = score_of_happiness(elements, set_A, set_B)
    print("Happiness:", happiness)
    
    
