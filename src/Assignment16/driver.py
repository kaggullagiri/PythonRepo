from src.Assignment16.util import to_check_piling

if __name__ == "__main__":
    T = int(input("Enter the number of test cases: "))

    test_cases = [(int(input()), list(map(int, input().split()))) for i in range(T)]

    results = to_check_piling(test_cases)

    print("\n".join(results))