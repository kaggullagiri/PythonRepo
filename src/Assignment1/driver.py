
from src.Assignment1.util import listproblem

if __name__ == '__main__':
    N = int(input("Enter the no.of commands: "))
    user_commands = [input().split() for i in range(N)]
    listproblem(user_commands)
    
