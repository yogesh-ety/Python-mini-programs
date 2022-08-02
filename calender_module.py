import calendar
import datetime
import time
#showing weekdays
print(calendar.weekheader(3))
print()

#showing index num of weekdays
print(calendar.firstweekday())
print()

#prints the respective month
print(calendar.month(2020,6,3))

#prints a 2D array consisting of days of a month
print(calendar.monthcalendar(2020,3))

#prints the year calendar
print(calendar.calendar(2020))

#prints the index num of the respective day mentioned
day_of_the_week=calendar.weekday(2020,6,16)
print(day_of_the_week)

#leap year
is_leap = calendar.isleap(2020)
print(is_leap)

#prints No of leap urs btw the yrs in parameter
how_many_leap_days = calendar.leapdays(2014,2024)
print(how_many_leap_days)
