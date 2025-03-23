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
'''

import sys

def leap_year(year: int) -> bool:
    """Determines if a given year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def mon_max(month: int, year: int) -> int:
    """Returns the maximum number of days in a given month."""
    days_per_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31,
                      8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if month == 2 and leap_year(year):
        return 29
    return days_per_month.get(month, 0)

def after(date: str) -> str:
    """Returns the next day's date in YYYY-MM-DD format."""
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
    """Checks if the given date is valid in YYYY-MM-DD format."""
    try:
        year, month, day = map(int, date.split('-'))
        return 1 <= month <= 12 and 1 <= day <= mon_max(month, year)
    except ValueError:
        return False

def day_of_week(year: int, month: int, date: int) -> str:
    """Determines the day of the week for a given date."""
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    offset = {1: 0, 2: 3, 3: 2, 4: 5, 5: 0, 6: 3, 7: 5, 8: 1, 9: 4, 10: 6, 11: 2, 12: 4}
    if month < 3:
        year -= 1
    num = (year + year // 4 - year // 100 + year // 400 + offset[month] + date) % 7
    return days[num]

def day_count(start_date: str, stop_date: str) -> int:
    """Counts the number of weekends (Saturdays and Sundays) in a given date range."""
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
    """Prints a usage message and exits."""
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
    Checks if the given date is valid in 'YYYY-MM-DD' format.
    Parameters:
        date (str): The date as a string in 'YYYY-MM-DD' format.
    Returns:
        bool: True if the date is valid, False otherwise.
    """

    try:
        # Ensure the date is in correct format
        parts = date.split('-')
        if len(parts) != 3:
            return False

       # Convert string parts to integers
        year, month, day = map(int, parts)

        # Validate year range (reasonable limits)
        if year < 1000 or year > 9999:  
            return False

        # Validate month range
        if month < 1 or month > 12:
            return False

       # Validate day range using mon_max()
        max_days = mon_max(month, year)
        if day < 1 or day > max_days:
            return False

        return True  # If all checks pass, return True

    except (ValueError, TypeError):
        return False  # Catch non-numeric value or the incorrect format
