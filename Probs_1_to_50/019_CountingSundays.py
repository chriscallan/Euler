# Problem 19
# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

from datetime import datetime, date

final_count = 0
for my_year in range(1901, 2001):
    for my_month in range(1, 13):
        if datetime(my_year, my_month, 1).weekday() == 6:
            print("{0} was a Sunday on the first of the month".format(datetime(my_year, my_month, 1)))
            final_count += 1

print("There were {0} Sundays that fell on the first of the month in the 20th century.".format(final_count))