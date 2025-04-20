try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)

except ValueError as e:
    print("Invalid input! Please enter a number:", e)

except ZeroDivisionError as e:
    print("Cannot divide by zero:", e)

except Exception as e:
    print("An unexpected error occurred:", e)

finally:
    print("Execution completed. Cleaning up resources if necessary.")
