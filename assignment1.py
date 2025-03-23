#!/usr/bin/env python3

'''
OPS445 Assignment 1 - Winter 2025
Program: assignment1.py 
Author: SUYASH MISHRA (SMISHRA27)
The python code in this file (a1_[Student_id].py) is original work written by
"Student Name". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
USAGE: 
	python3 assignment1.py 2023-05-01 2023-05-30
'''

import sys

def leap_year(year: int) -> bool:
    """Finding if the year is leap year or not"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
#Confirming that we have leap year or not by divisibilty of 4

def mon_max(month: int, year: int) -> int:
    """FInding the maximum number of days in a given month."""
    days_per_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31,
                      8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if month == 2 and leap_year(year):
        return 29
    return days_per_month.get(month, 0)
#Output is month max no. of days

def after(date: str) -> str:
    """The After function is used to delay execution of the program or to execute a command in background sometime in the future. 
	But we can build a loop inside the mainloop by calling itself.Returns the next day's date in YYYY-MM-DD format."""
    year, month, day = map(int, date.split('-'))
    day += 1
    if day > mon_max(month, year):
        day = 1
        month += 1
    if month > 12:
        month = 1
        year += 1
    return f"{year:04d}-{month:02d}-{day:02d}"

def valid_date(date: str) -> bool:
    """We check if the given date is valid in YYYY-MM-DD format."""
    try:
        year, month, day = map(int, date.split('-'))
        return 1 <= month <= 12 and 1 <= day <= mon_max(month, year)
    except ValueError:
        return False #Ensuring that we have valid date for further calculation

def day_of_week(year: int, month: int, date: int) -> str:
    """Determining the day of the week for a given date."""
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    offset = {1: 0, 2: 3, 3: 2, 4: 5, 5: 0, 6: 3, 7: 5, 8: 1, 9: 4, 10: 6, 11: 2, 12: 4}
    if month < 3:
        year -= 1
    num = (year + year // 4 - year // 100 + year // 400 + offset[month] + date) % 7
    return days[num]

def day_count(start_date: str, stop_date: str) -> int:
    """Counting the number of weekends (Saturdays and Sundays) in a given date range."""
    count = 0
    current_date = min(start_date, stop_date)
    stop_date = max(start_date, stop_date)
    while current_date <= stop_date:
        year, month, day = map(int, current_date.split('-'))
        if day_of_week(year, month, day) in ['sat', 'sun']:
            count += 1
        current_date = after(current_date)
    return count

def usage():
    """Getting output in a usage message and exits."""
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()
    date1, date2 = sys.argv[1], sys.argv[2]
    if not valid_date(date1) or not valid_date(date2):
        usage()
    weekends = day_count(date1, date2)
    print(f"The period between {min(date1, date2)} and {max(date1, date2)} includes {weekends} weekend days.")

def valid_date(date: str) -> bool:
    """
    We here check if the given date is valid in 'YYYY-MM-DD' format.
    Parameters I used here are
        date (str): The date as a string in 'YYYY-MM-DD' format.
    Returning as
        bool: True if the date is valid, False otherwise.
    """

    try:
        # Ensuring the date is in correct format
        parts = date.split('-')
        if len(parts) != 3:
            return False

       # Converting string parts to integers
        year, month, day = map(int, parts)

        # Validating year range within reasonable limit
        if year < 1000 or year > 9999:  
            return False

        # Validating month range
        if month < 1 or month > 12:
            return False

       # Validating day range using mon_max()
        max_days = mon_max(month, year)
        if day < 1 or day > max_days:
            return False

        return True  # If all checks pass, return True

    except (ValueError, TypeError):
        return False  # Catching any non-numeric value or the incorrect format

def day_count(start_date: str, end_date: str) -> int:
    """
    Here we loop through a range of dates, and returns the number of weekend days.
    Parameters I used here are 
        start_date (str): The start date in 'YYYY-MM-DD' format.
        end_date (str): The end date in 'YYYY-MM-DD' format.
    Returning as
        int: The number of weekend days in the given range.
    """
    count = 0
    current_date = min(start_date, end_date)  # Ensuring correct order
    end_date = max(start_date, end_date)

    # Loop until the current date exceeds the end date
    while current_date <= end_date:
        year, month, day = map(int, current_date.split('-'))
        weekday = day_of_week(year, month, day)  # Get day of the week

        # Counting if it's Saturday or Sunday
        if weekday in ['sat', 'sun']:
            count += 1

        current_date = after(current_date)  # Moving to the next day
    return count

if __name__ == "__main__":
    # Checking if the right number of arguments are passed
    if len(sys.argv) != 3:
        usage()

    start_date = sys.argv[1]
    end_date = sys.argv[2]

    # Checking if both dates are valid
    if not valid_date(start_date) or not valid_date(end_date):
        usage()

    # Ensuring start date is earlier than end date
    if start_date > end_date:
        start_date, end_date = end_date, start_date  # Swap if dates are in the wrong order

    # Calculating the number of weekend days
    weekend_days = day_count(start_date, end_date)

    # Finally we can get the ouput of number of weekends between dates
    print(f"The number of weekend days between {start_date} and {end_date} is: {weekend_days}")
