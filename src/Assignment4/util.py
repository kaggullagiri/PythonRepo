
import calendar
def Findingday(month, day, year):
    res = calendar.weekday(year, month, day)
    return calendar.day_name[res].upper()
    
