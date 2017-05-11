from functools import reduce
# compute a salary threshold

# 90 30 100 40 20

# target payroll 210

# then 60 is a suitable salary cap since 60 + 30 + 60 + 40 + 20

# sort it
# get the current average salary
# get the wanted average salary
# find the salaries above the wanted average salary
# sum the salaries that are above the average salary
# subtract the difference between current payroll and desired payroll then get the average. set that to the new cap

# constraints
# assume all salaries are > 0 and the sum of salaries is > target_payroll

# Time: O(nlogn + n)

def compute_salary_threshold(salaries, target_payroll):
    salaries.sort()
    current_payroll = 0
    for salary in salaries:
        current_payroll += salary
    avg_salary = current_payroll / len(salaries)

    desired_avg_salary = target_payroll / len(salaries)
    salaries_above_wanted_average_salary = [salary for salary in salaries if salary > desired_avg_salary]
    sum_of_salaries_above_wanted_average_salary = reduce((lambda x, y: x + y), salaries_above_wanted_average_salary)

    payroll_difference = abs(target_payroll - current_payroll)
    salary_cap = (sum_of_salaries_above_wanted_average_salary - payroll_difference)/len(salaries_above_wanted_average_salary)


    return salary_cap

# Test
assert 60 == compute_salary_threshold([90, 30, 100, 40, 20], 210)
