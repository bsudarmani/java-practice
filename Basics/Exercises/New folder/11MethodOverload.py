class Calculator:
    # Method that simulates overloading using *args
    def add(self, *args):
        if not args:
            return 0
        else:
            result = 0
            for num in args:
                result += num
            return result

# Create object
calc = Calculator()

print("No arguments:", calc.add())               # 0
print("Two arguments:", calc.add(10, 20))         # 30
print("Three arguments:", calc.add(1, 2, 3))      # 6
print("Five arguments:", calc.add(5, 10, 15, 20, 25))  # 75
