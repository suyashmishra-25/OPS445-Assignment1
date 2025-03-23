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
 
def day_of_week(date: str) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    day, month, year = (int(x) for x in date.split('/'))
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + day) % 7
    return days[num]
 
def mon_max(month: int, year: int) -> int:
   """Returning the max day in a month. Incl leap year check"""
    feb_max = 29 if leap_year(year) else 28
    days_in_month = {
        1: 31, 2: feb_max, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31,
        8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    return days_in_month.get(month, 0) 

def after(date: str) -> str:
    """
    Computes the date of the following day for a given date in 'YYYY-MM-DD' format.
    """
    year, month, day = map(int, date.split('-'))
    
    if day < mon_max(month, year):
        day += 1
    else:
        day = 1
        month += 1
    
    if month > 12:
        month = 1
        year += 1
    
    return f"{year:04d}-{month:02d}-{day:02d}"
 
def usage():
    """
    Displays usage instructions and exits if incorrect arguments are provided.
    """
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")
    sys.exit(1)

def leap_year(year: int) -> bool:
    """
    Determines whether a given year is a leap year.
    Returns True if leap year, otherwise False.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) 
 
def valid_date(date: str) -> bool:
    "check validity of date and return True if valid"
    ...
 
 
def day_count(start_date: str, stop_date: str) -> int:
    "Loops through range of dates, and returns number of weekend days"
    ...
 
 
if __name__ == "__main__":
    ...
