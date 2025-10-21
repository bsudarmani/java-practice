def Arithmetic(a,b,op):
    if op == '+':
        return f"Addition {a} + {b} = {a+b}"
    elif op == '-':
        return f"Subtraction {a} - {b} = {a - b}"
    elif op == '/':
        if(b==0):
            raise ValueError("Infinity")
        else:
            return f"Division {a} / {b} = {a/b}"
    elif op == '*':
        return f"Multiplication {a} * {b} = {a * b}"
    else:
        raise ValueError("Invalid Operator")

def Logic():
    try:
        a = int(input("Enter num 1:"))
        b= int(input("Enter num 2:"))
        op = input("Enter Operator (+,-,/,*):")
        res = Arithmetic(a,b,op)
        print(res)
        ch = input("Did you want to continue(Y/N): ")
        if ch== 'y' or ch=='Y':
            Logic()
    except ValueError as e:
        print(e)
        Logic()

Logic()

    
