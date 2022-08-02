import datetime
import pytz

today = datetime.date.today()
print(today)
print(today.day)
print(today.weekday())

# datetime.time (hr ,min ,sec ,msec )
# datetime.date (yr ,mon ,date)
# datetime.datetime (yr ,mon ,date ,hr ,min ,sec ,msec)

date_time = datetime.datetime.today()
print(date_time)

birthday = datetime.date(2002, 3, 18)
print(birthday)

days_since_birth = (today - birthday).days
print(days_since_birth)

# adding or subtracting days and time
tdelta = datetime.timedelta(days=10)
print(today + tdelta)

hrdelta = datetime.timedelta(hours=10)
print(datetime.datetime.now() + hrdelta)

# time zone of all the countries
for tz in pytz.all_timezones:
    print(tz)

# time zone
datetime_today = datetime.datetime.now(tz=pytz.UTC)
print(datetime_today)
datetime_pacific = datetime_today.astimezone(pytz.timezone('US/pacific'))
print(datetime_pacific)

# string FORMATTING using dates
# 27-06-2020 --> jun 27 ,20
print(datetime_pacific.strftime('%b %d ,%y'))

# 27-06-2020 --> june 27 ,2020
print(datetime_pacific.strftime('%B %d ,%Y'))

# string PARSING
# june 09 , 2019 --> datetime(2020 ,3 ,9)
date_thing = datetime.datetime.strptime("jun 03 2020" , '%b %d %Y')
print(date_thing)
print(repr(date_thing))
