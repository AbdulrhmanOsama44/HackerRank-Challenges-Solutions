import calendar
def guess_day(month, day, year):
    week_day = calendar.weekday(year, month, day)
    return calendar.day_name[week_day].upper()
   
month, day, year = list(map(int, input().split())) 
print(guess_day(month, day, year))