from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

print(timedelta(days=365,hours=5,minutes=1))

now = datetime.now()
print("Today is: " + str(now))

#Calculates the date one year from now using the days specified in the function.
print("One year from now it will be "+ str(now+timedelta(days=365)))

#Calculates the date using two arguments.
print("In 2 days and 3 weeks it will be "+ str(now+timedelta(days=2,weeks=3)))

#Calculates the date in past.
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print("One week ago it was: " +s)

