from src.Assignment19.util import Iterables_and_Iterators_probability

if __name__ == "__main__":
    N = int(input("Enter the number of letters: "))
    letters = list(input("Enter the letters separated by space: ").split())
    K = int(input("Enter the value of K: "))
    target_letter = input("Enter the target letter: ")

    probability = Iterables_and_Iterators_probability(letters, K, target_letter)

    print(f"Probability of '{target_letter}' in combinations of size {K}: {probability:.4f}")