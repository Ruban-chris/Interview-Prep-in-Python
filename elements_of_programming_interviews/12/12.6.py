# compute the real square root

# input floating point value
# return the square root
# degrees of precision? assume 3 decimal places of precision
import math
def sqrt(number):
    lower_bound, upper_bound = (number, 1.0) if number < 1.0 else (1.0, number)

    while not math.isclose(lower_bound, upper_bound):
        mid = 0.5 * (lower_bound + upper_bound)
        mid_squared = mid * mid
        if mid_squared > number:
            upper_bound = mid
        if mid_squared < number:
            lower_bound = mid
    return lower_bound

print(sqrt(5))
print(sqrt(0.5))
