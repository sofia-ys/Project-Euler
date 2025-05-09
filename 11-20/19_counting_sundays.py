# a leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400
def leapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)  # returns whether this statement is true or false

# list with how many days each month has
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]

# check if a day number i is a sunday
def firstSunday(i, week):
    return week[i % len(week)] == "sun"

# check how many sundays we have in a year
def yearSunday(startDay, week, months, year):
    sum = 0
    day = startDay  # the day we start with depends on what day the year starts with
    if leapYear(year):  # if it's a leap year feb will have 29 days
        months[1] = 29
    for month in months:
        if firstSunday(day, week):  # checking if the first of the month is a sunday
            sum += 1
        day += month  # adding a month to the day such that we only check the first of the month
    return sum

# initialising conditions, 1901 started on a tuesday
sundayCount = 0
year = 1901
startDay = 2

for i in range(99):  # over the 100 period
    sundayCount += yearSunday(startDay, week, months, year)  # check how many sundays are in that year

    year = 1901 + i  # add the number of years that's passed since the start
    if leapYear(year):
        days = 366
    else:
        days = 365
    
    startDay += days  # add however many days we've passed now to our start date

print(sundayCount)


