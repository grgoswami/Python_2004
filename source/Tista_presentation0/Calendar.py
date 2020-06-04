import calendar
import random

month = int(input('Enter a month(Enter the month number): '))
year  = int(input('Enter a year: '))
 
if month == 12 or month < 12:
    print (calendar.month(year, month))

if month > 12:
    month0 = int(input("Please enter a month's number that is more than 0 and less than 13: "))
    print (calendar.month(year, month0))

year_list = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
year_list0 = list(range(1990,2020))
month_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
month_list0 = list(range(1,13))

print(year_list0)
print(month_list0)
random_month = random.choice(month_list)
random_year = random.choice(year_list)

calendar.prmonth(random_year, random_month, 2, 1)

