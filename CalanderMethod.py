# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

month, day, year = map(int, input().split())

weekday = calendar.weekday(year, month, day)

print(calendar.day_name[weekday].upper())

#input 08 05 2015
#output WEDNESDAY
