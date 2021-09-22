import datetime

my_time = datetime.datetime.now()

print(my_time)

#manejo de dia actual
my_day = datetime.date.today()

print(' year: {year} \n month: {month} \n day: {day}'.format(
    year=my_day.year,
    month=my_day.month,
    day=my_day.day
))

#manejo de formato de fechas
my_time = my_time.strftime('%d %m %Y')
print(my_time)

