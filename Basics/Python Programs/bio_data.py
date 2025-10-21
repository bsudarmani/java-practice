import os
print("\tBio Data")
name=input("Enter your name:")
age=input("Enter your age:")
gender=input("Enter your gender:")
dob=input("Enter your date of birth:")
mobile=input("Enter your mobile:")
email=input("Enter your email:")
father=input("Enter your father name:")
mother=input("Enter your mother name:")
aim=input("Enter your aim:")
hobby=input("Enter your hobby:")
qual=input("Enter your qualification:")

def  Validate():
    if len(mobile) != 10:
        raise ValueError("Mobile number should contain 10 digit")
    if not("@" in email):
        raise ValueError("email should contain @ symbol")
        
os.system("cls")
try:
    Validate()
    print("\tBIO DATA")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Gender: {gender}")
    print(f"DOB: {dob}")
    print(f"Mobile: {mobile}")
    print(f"Email: {email}")
    print(f"Father Name: {father}")
    print(f"Mother Name: {mother}")
    print(f"Aim: {aim}")
    print(f"Hobby: {hobby}")
    print(f"Qualification: {qual}")
except ValueError as e:
    print(e)

