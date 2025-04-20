import sqlite3

try:
    conn = sqlite3.connect("satheesh.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Employee (
            emp_id INTEGER PRIMARY KEY,
            emp_name TEXT NOT NULL,
            designation TEXT NOT NULL,
            salary INTEGER NOT NULL
        )
    """)
    print("Table Created Successfully")

    print("\nChoose Operation:")
    print("1. Insert")
    print("2. Update")
    print("3. Delete")
    print("4. Select")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':  # Insert
        try:
            emp_id = int(input("Enter Employee ID: "))
            emp_name = input("Enter Employee Name: ")
            designation = input("Enter Designation: ")
            salary = int(input("Enter Salary: "))
            cursor.execute("INSERT INTO Employee(emp_id, emp_name, designation, salary) VALUES (?, ?, ?, ?)", 
                           (emp_id, emp_name, designation, salary))
            conn.commit()
            print("Record inserted successfully")
        except Exception as e:
            print(f"Insert error: {e}")

    elif choice == '2':  # Update
        try:
            emp_id = int(input("Enter Employee ID to update: "))
            new_designation = input("Enter new Designation: ")
            cursor.execute("UPDATE Employee SET designation = ? WHERE emp_id = ?", 
                           (new_designation, emp_id))
            conn.commit()
            print("Record updated successfully")
        except Exception as e:
            print(f"Update error: {e}")

    elif choice == '3':  # Delete
        try:
            emp_id = int(input("Enter Employee ID to delete: "))
            cursor.execute("DELETE FROM Employee WHERE emp_id = ?", (emp_id,))
            conn.commit()
            print("Record deleted successfully")
        except Exception as e:
            print(f"Delete error: {e}")

    elif choice == '4':  # Select
        cursor.execute("SELECT * FROM Employee")
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(f"Emp_id: {row[0]}, Name: {row[1]}, Designation: {row[2]}, Salary: {row[3]}")
        else:
            print("No records found")
        print("Data retrieved successfully")

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")

except Exception as e:
    print(f"Error: {e}")

finally:
    conn.close()
    print("Connection Closed")
