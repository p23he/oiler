# You are given the following information, but you may prefer to do some research for yourself.

#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a #century unless it is divisible by 400.
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

year = 1901
sunday = 6
month = 1

def is_leap(year):
  if year % 100 == 0:
    return year % 400 == 0
  else:
    return year % 4 == 0

sum = 0
days = 31

while year <= 2000:

  if month == 9 or month == 4 or month == 6 or month == 11:
    days = 30
  elif month == 2:
    if is_leap(year):
      days = 29
    else:
      days = 28
  else:
    days = 31

  if sunday == 1:
    sum += 1
  
  if sunday + 7 > days:
    sunday += 7 - days
    month += 1
  else:
    sunday += 7
  if month > 12:
    year += 1
    month = 1
  print(month, sunday, year)
print(sum)
