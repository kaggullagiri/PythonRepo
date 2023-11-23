# driver.py
from util import Findingday

if __name__ == '__main__':
    month, day, year = map(int, input("Enter mm/dd/yyyy : ").split())
    result = Findingday(month, day, year)
    print('Today is ',result)
    
