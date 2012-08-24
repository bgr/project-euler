# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

days_in_months = [31,None,31,30,31,30,31,31,30,31,30,31]

day_in_week = 0
sundays = 0
for year in range(1900, 2001):
  is_leap = (year%100!=0 and year%4==0) or (year%100==0 and year%400==0)
  for m in range(12):
    days_in_this_month = days_in_months[m] if m!=1 else 29 if is_leap else 28
    for date in range(days_in_this_month):
      if date==0 and day_in_week==6 and year>1900:
        sundays += 1
      day_in_week = (day_in_week+1) % 7
      
print sundays