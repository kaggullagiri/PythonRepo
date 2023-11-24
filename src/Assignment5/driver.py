from src.Assignment5.util import StringMutation

if __name__ == '__main__':
    st = input("Enter the stringName: ")
    i, c = input("Enter the position & character separated by space: ").split()
    new_string = StringMutation(st, int(i), c)
    print("The modified string is string:", new_string)
    


    

