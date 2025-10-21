class Execute:
    def exec(self,a,b,op):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return a / b
        elif op == '%':
            return a % b
        else:
            raise ValueError("Invalid Input")
class Arith(Execute):
    def __init__(self):
        print("\tARITHMETIC OPERATION  ")
        self.main()
        print("THANK YOU")
    def main(self):
        while True:
            try:
                self.a = int(input("Enter num 1: "))
                self.b = int(input("Enter num 2:"))
                self.op = input("Enter a operator: ")
                print(f"{self.a} {self.op} {self.b} = {self.exec(self.a,self.b,self.op)}")
            except Exception as e:
                print(f"Error: {e}")
            finally:
                if input("Do you want to continue(Y/N):")[0].lower() != 'y':
                    break

a = Arith()
