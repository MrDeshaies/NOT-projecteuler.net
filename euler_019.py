from datetime import date

# How many Sundays fell on the first of the month
# during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

SUNDAY = 6

hit = 0
for year in range(1901,2001):
    for month in range(1,13):
        if date(year,month,1).weekday() == SUNDAY:
            hit += 1
print(hit)
