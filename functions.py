from database import employee_data
import random
def display_details(employeeID: int):

    last_name = employee_data[employeeID][0]
    first_name = employee_data[employeeID][1]
    full_name = first_name + " " + last_name
    date_of_birth = employee_data[employeeID][2]
    hourly_rate = employee_data[employeeID][3]

    print("")
    print(f"Employee ID: {employeeID}")
    print(f"Employee Name: {full_name}")
    print(f"Date of birth: {date_of_birth}")
    print(f"Hourly rate: {hourly_rate}")
    print("")

# def generate_total_hours():
#     total_hours = random.randrange(70, 90)
#     return total_hours

def calculate_gross (employeeID, hours_worked):
    hourly_rate = float(employee_data[employeeID][3])
    rice_subsidy = 1500
    phone_allowance = float(employee_data[employeeID][4])
    clothing_allowance = float(employee_data[employeeID][5])
    total_gross = round((hourly_rate * hours_worked) + rice_subsidy + phone_allowance + clothing_allowance, 2)
    return total_gross

def calculate_sss(income: float):
    last_range = 24750
    maximum_contribution = 1125.00
    # Calculate the total contribution if income is within the specified range
    if income <= last_range:
        # Define contribution per range
        contribution_per_range = 22.50
        # Calculate the number of ranges the compensation falls into
        range_count = (income - 3250) // 500
        # Ensure range_count is within bounds
        range_count = max(0, min(range_count, 44))
        # Calculate the total contribution
        total_contribution = 135.00 + range_count * contribution_per_range
    else:
        total_contribution = maximum_contribution
    return round(total_contribution, 2)

def calculate_pagibig(income: float):
    employee_contribution = 0
    if income > 1500:
        employee_contribution = income * 0.02
    else:
        employee_contribution = income * 0.01
    return round(employee_contribution, 2)

def calculate_phileath(income: float):
    return round(((income * 0.03) / 2), 2)

def calcuate_witholdingTax(income: float):
    sss = calculate_sss(income)
    pagibig = calculate_pagibig(income)
    philhealth = calculate_phileath(income)
    total_deductions = sss + pagibig + philhealth
    taxable_income = income - total_deductions
    if taxable_income <= 20832:
        tax = 0
    elif 20833 <= taxable_income < 33333:
        tax = (taxable_income - 20833) * 0.20
    elif 33333 <= taxable_income < 66667:
        tax = 2500 + (taxable_income - 33333) * 0.25
    elif 66667 <= taxable_income < 166667:
        tax = 10833 + (taxable_income - 66667) * 0.30
    elif 166667 <= taxable_income < 666667:
        tax = 40833.33 + (taxable_income - 166667) * 0.32
    else:
        tax = 200833.33 + (taxable_income - 666667) * 0.35
    return round(tax, 2)

def calculate_net(gross: float, withholding_tax):
    return gross - withholding_tax



