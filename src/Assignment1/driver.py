# driver.py

from util import process_commands


def listprgm():
    N = int(input('Enter how many times you need to perform operation: '))
    E_list = []

    for i in range(N):
        command = input().split()
        process_commands(E_list, command)


if __name__ == '__main__':
    listprgm()


