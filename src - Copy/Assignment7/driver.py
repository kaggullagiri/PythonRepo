from util import split_num_char

if __name__ == '__main__':
    string, k = input("Enter the String Value= "), int(input("Enter the Key Value= "))
    result = list(split_num_char(string, k))
    for word in result:
        print(word)