def write_emp_details(file_name):
    with open(file_name, 'a') as file:
        while True:
            print("\nEnter employee details:")
            emp_id = input("Employee ID: ")
            name = input("Name: ")
            designation = input("Designation: ")
            salary = input("Salary: ")

            file.write(f"{emp_id},{name},{designation},{salary}\n")
            print("Employee details saved successfully.")

            cont = input("Do you want to add another employee? (y/n): ").strip().lower()
            if cont != 'y':
                break


def read_emp_details(file_name):
    try:
        with open(file_name, 'r') as file:
            print("\nEmployee Details:")
            print(f"{'ID':<10}{'Name':<20}{'Designation':<20}{'Salary':<10}")
            print("-" * 60)
            for line in file:
                emp_id, name, designation, salary = line.strip().split(',')
                print(f"{emp_id:<10}{name:<20}{designation:<20}{salary:<10}")
    except FileNotFoundError:
        print("No employee records found. Please add employees first.")

#main
file_name = "employee_details.txt"
while True:
    print("1. Add Employee Details")
    print("2. View Employee Details")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == '1':
        write_emp_details(file_name)
    elif choice == '2':
        read_emp_details(file_name)
    elif choice == '3':
        print("Exit")
        break
    else:
        print("Invalid choice. Please try again.")


