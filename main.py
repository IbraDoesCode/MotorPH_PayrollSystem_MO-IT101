from functions import *
from database import employee_data
from art import logo

print(logo)

while True:
    print("\n=== MENU ===")
    print("1. View employee details")
    print("2. Calculate gross income")
    print("3. Calculate net salary")
    print("4. Exit")

    action = input("Enter your choice (1/2/3/4): ")

    if action == "1":
        emp_ID = int(input("Enter employee ID: "))
        if emp_ID not in employee_data:
            print("Employee ID not found. Please try again.")
            continue
        display_details(emp_ID)

    elif action == "2":
        emp_ID = int(input("Enter employee ID: "))
        if emp_ID not in employee_data:
            print("Employee ID not found. Please try again.")
            continue
        hours_worked = float(input("Enter hours worked: "))
        gross = calculate_gross(emp_ID, hours_worked)
        hourly_rate = float(employee_data[emp_ID][3])
        print(f"\nHourly rate: {hourly_rate}")
        print(f"Hours worked: {hours_worked}")
        print(f"Total Gross: {gross}")

    elif action == "3":
        emp_ID = int(input("Enter employee ID: "))
        if emp_ID not in employee_data:
            print("Employee ID not found. Please try again.")
            continue
        hours_worked = float(input("Enter hours worked: "))
        gross = calculate_gross(emp_ID, hours_worked)
        sss = calculate_sss(gross)
        pagibig = calculate_pagibig(gross)
        philhealth = calculate_philhealth(gross)
        total_deductions = sss + pagibig + philhealth
        withholding_tax = calculate_withholdingTax(gross)
        net_salary = round(calculate_net(gross, withholding_tax), 2)

        print("\n--- Net Salary Details ---")
        print(f"Gross income: {gross}")
        print(f"SSS contribution: {sss}")
        print(f"Pag-IBIG contribution: {pagibig}")
        print(f"PhilHealth contribution: {philhealth}")
        print(f"Withholding tax: {withholding_tax}")
        print(f"Net salary: {net_salary}")

    elif action == "4":
        print("Exiting the system...")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
