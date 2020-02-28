"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    
    # Calculation of the number of days
    if (1 <= month <= 11): 
        date1 = datetime.date(year,month,1)
        date2 = datetime.date(year,month+1,1)
        return (date2 - date1).days
    elif (month == 12):
        return 31
    
def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    
    # verification of the date
    if (datetime.MINYEAR <= year <= datetime.MAXYEAR):
        if (1 <= month <= 12):
            if (0 < day <= days_in_month(year,month)):
                return True
            else:
                return False # day is not valid
        else:
            return False # month is not valid
    else:
        return False # year is not valid

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    
    # Calculation of the days between
    if (is_valid_date(year1,month1,day1) and is_valid_date(year2,month2,day2)):
        date1 = datetime.date(year1,month1,day1)
        date2 = datetime.date(year2,month2,day2)
        if (date2 >= date1):
            return (date2 - date1).days # days between date2 and date1
        else:
            return 0 # date2 < date1
    else:
        return 0 # The date is invalid

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    if (is_valid_date(year,month,day)):
        today = datetime.date.today()
        birthdate = datetime.date(year,month,day)
        if (birthdate < today):
            return days_between(year,month,day,today.year,today.month,today.day)        
        else:
            return 0 # date is in the futur
    else:
        return 0 # date is not valid

# program    
print("days in month:", days_in_month(2019,12))
print("is valid date:", is_valid_date(2019,2,28))
print("days between:", days_between(1972,11,18,2019,9,24))
print("age in days:", age_in_days(0,11,18))
