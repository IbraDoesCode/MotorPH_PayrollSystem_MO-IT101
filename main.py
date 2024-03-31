from functions import *
from data import *
from art import logo

print(logo)

while True:
    print("\n=== MENU ===")
    print("1. View employee details")
    print("2. View weekly attendance")
    print("3. Calculate weekly gross")
    print("4. Calculate weekly net")
    print("5. Exit")

    action = input("Enter your choice (1/2/3/4): ")

    if action == "1":
        emp_ID = int(input("Enter employee ID: "))
        display_details(emp_ID)

    elif action == "2":
        # To implement
        emp_ID = int(input("Enter employee ID: "))
        display_attendance(emp_ID)

    elif action == "3":
        emp_ID = int(input("Enter employee ID: "))
        hours_worked = calculate_hours_worked(emp_ID)
        gross = calculate_weekly_gross(emp_ID, hours_worked)
        rate = employee_data[emp_ID - 1]['hourly_rate']
        print(f"\nHourly rate: {rate}")
        print(f"Hours worked: {hours_worked:.2f}")
        print(f"Total Gross: {gross}")

    elif action == "4":
        emp_ID = int(input("Enter employee ID: "))
        hours_worked = calculate_hours_worked(1)
        gross = calculate_weekly_gross(emp_ID, hours_worked)
        monthly = employee_data[emp_ID-1]["basic_salary"]
        sss = calculate_sss(gross)
        pagibig = calculate_pagibig(monthly)
        philhealth = calculate_philhealth(monthly)
        total_deductions = sss + pagibig + philhealth
        tax = calculate_withholding_tax(gross, sss, pagibig, philhealth)
        net_salary = round(calculate_net(gross, tax), 2)

        print("\n--- Net Salary Details ---")
        print(f"Gross income: {gross}")
        print(f"SSS contribution: {sss}")
        print(f"Pag-Ibig contribution: {pagibig}")
        print(f"PhilHealth contribution: {philhealth}")
        print(f"Withholding tax: {tax}")
        print(f"Net salary: {net_salary}")

    elif action == "5":
        print("Exiting the system...")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
