
from src.Assignment3.util import second_highest

def Secondhighest():
    n = int(input("Enter how many students , after that enter scores finding runnerup : "))
    arr = map(int, input().split())
    runner_up = second_highest(arr)
    print(runner_up)

if __name__ == '__main__':
    Secondhighest()