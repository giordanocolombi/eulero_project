# Giordano Colombi 05-12-2019
  
# ---------------------- EXERCISE TEXT ---------------------- #
# The sum of the squares of the first ten natural numbers is,
#            1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#            (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the 
#first ten natural numbers and the square of the sum is:
#                    3025 − 385 = 2640.
# Find the difference between the sum of the squares of the 
# first one hundred natural numbers and the square of the sum.
# ----------------------------------------------------------- #

def sum_of_squares(_from, _to):
    return sum(i**2 for i in range(_from, _to +1))

def square_of_sum(_from, _to):
    return sum(range(_from, _to +1))**2

if __name__ == "__main__":
    _from = 1
    _to = 100
    result = square_of_sum(_from, _to) - sum_of_squares(_from, _to)
    print("----> the solution is: {}".format(result))
