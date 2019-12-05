# Giordano Colombi 05-12-2019
  
# ---------------------- EXERCISE TEXT ---------------------- #
# You are given the following information, but you may prefer 
# to do some research for yourself:
# - 1 Jan 1900 was a Monday.
# - Thirty days has September,
# - April, June and November.
# - All the rest have thirty-one,
# - Saving February alone,
# - Which has twenty-eight, rain or shine.
# - And on leap years, twenty-nine.
# - A leap year occurs on any year evenly divisible by 4, but 
#   not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the 
# twentieth century (1 Jan 1901 to 31 Dec 2000)?
# ----------------------------------------------------------- #

import numpy as np

dict_months = {
    "january": 31,
    "february": 28,
    "march": 31,
    "april": 30,
    "may": 31,
    "june": 30,
    "july": 31,
    "august": 31,
    "september": 30,
    "october": 31,
    "november": 30,
    "december": 31
}

def find_first_day_month(_from, _to):
    arr = np.array([])
    fist_day = 1
    for i in range(_from, _to + 1):
        for k in dict_months:
            if ((i % 400 == 0) or (i % 4 == 0 and i % 100 != 0 )) and (k == "february"):
                fist_day += dict_months[k] + 1
            else: 
                fist_day += dict_months[k]
            arr =  np.append(arr, fist_day)
    return arr

def sum_of_squares(_from, _to):
    return sum(i**2 for i in range(_from, _to + 1))

def square_of_sum(_from, _to):
    return sum(range(_from, _to + 1))**2

def count_leap_years(_from, _to):
    return sum(True for i in range(_from, _to + 1) if (i % 400 == 0) or (i % 4==0 and i % 100 != 0))

def count_number_of_days(_from, _to):
    return 365*(_to-_from+1) + count_leap_years(_from, _to)

def find_multiples(n, _from, _to):
    return np.array([i for i in range(_from, _to+1) if i%n==0])


if __name__ == "__main__":
    _from = 1900
    _to = 2000

    tot = total_number_of_days(1900,2000)
    multiples = find_multiples(7, 1, tot)
    first_days = find_first_day_month(_from, _to)

    n_sundays = len(set(multiples[multiples > 365]).intersection(set(first_days[first_days > 365])))
    print("----> the solution is: {}".format(result))