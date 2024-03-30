from data import *


def display_details(empid: int):
    index = empid - 1
    if 0 <= index < len(employee_data):
        employeeID = index
        employee_name = f"{employee_data[employeeID]['first_name']} {employee_data[employeeID]['last_name']}"
        birthday = employee_data[employeeID]['date_of_birth']
        # Display details to console
        print("\n")
        print(f"EmployeeID: {employeeID + 1}")
        print(f"Employee Name: {employee_name}")
        print(f"Date of birth: {birthday}")
    else:
        print("Record does not exist")


def calculate_hours_worked(empid: int):
    total_hours = 0
    for data in attendance_data:
        if data.get('Employee_ID') == empid:
            # retrieve time in data
            time_in_data = data.get('Time_in').split(":")
            time_in_hour = int(time_in_data[0])
            time_in_minutes = int(time_in_data[1])
            # retrieve time out data
            time_out_data = data.get('Time_out').split(":")
            time_out_hour = int(time_out_data[0])
            time_out_minutes = int(time_out_data[1])

            hours_worked = (time_out_hour - time_in_hour) + (time_out_minutes - time_in_minutes) / 60
            total_hours += hours_worked
    return total_hours


def display_attendance(empid: int):
    print(f"Attendance records for Employee ID {empid}:")
    for data in attendance_data:
        if data.get('Employee_ID') == empid:
            print(f"Date: {data['Date']}, Time in: {data['Time_in']}, Time out: {data['Time_out']}\n")
    total_hours = calculate_hours_worked(empid)
    print(f"Total hours worked: {total_hours}")


def calculate_weekly_gross(empid, hours_worked):
    rate = employee_data[empid - 1]['hourly_rate']
    rice_subsidy = (1500 * 12) / 52  # calculate weekly rice subsidy
    weekly_gross = (rate * hours_worked) + rice_subsidy
    return round(weekly_gross, 2)


def calculate_sss(income: float):
    last_range = (24750 * 12) / 52
    max_contribution = (1125.00 * 12) / 52

    if income <= last_range:
        contribution_per_range = (22.50 * 12) / 52
        range_count = (income - (3250 * 12) / 52) // ((500 * 12) / 52)
        range_count = int(max(0, min(range_count, 44)))
        weekly_contribution = (135.00 * 12) / 52 + range_count * contribution_per_range
    else:
        weekly_contribution = max_contribution

    return round(weekly_contribution, 2)


def calculate_pagibig(monthly_basic: float):
    monthly_contribution = 0
    if monthly_basic > 1500:
        monthly_contribution = monthly_basic * 0.02
    else:
        monthly_contribution = monthly_basic * 0.01
    weekly_contribution = (monthly_contribution * 12) / 52
    return round(weekly_contribution, 2)


def calculate_philhealth(monthly_basic: float):
    monthly_contribution = (monthly_basic * 0.05) / 2
    weekly_contribution = (monthly_contribution * 12) / 52
    return round(weekly_contribution, 2)


def calculate_withholding_tax(weekly_income: float, sss: float, pagibig: float, philhealth: float):
    total_deductions = sss + pagibig + philhealth
    taxable_income = weekly_income - total_deductions

    if taxable_income <= 20832 / 4:
        tax = 0
    elif 20833 / 4 <= taxable_income < 33333 / 4:
        tax = (taxable_income - 20833 / 4) * 0.20
    elif 33333 / 4 <= taxable_income < 66667 / 4:
        tax = (2500 / 4) + (taxable_income - 33333 / 4) * 0.25
    elif 66667 / 4 <= taxable_income < 166667 / 4:
        tax = (10833 / 4) + (taxable_income - 66667 / 4) * 0.30
    elif 166667 / 4 <= taxable_income < 666667 / 4:
        tax = (40833.33 / 4) + (taxable_income - 166667 / 4) * 0.32
    else:
        tax = (200833.33 / 4) + (taxable_income - 666667 / 4) * 0.35

    return round(tax, 2)


def calculate_net(gross: float, withholding_tax):
    return gross - withholding_tax
