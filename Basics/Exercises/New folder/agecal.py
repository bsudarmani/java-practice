from datetime import date

try:
    date_input = input("Enter your birth date (dd/mm/yyyy): ")
    bdate, bmonth, byear = map(int, date_input.split('/'))
except ValueError:
    print("Invalid date format. Please use dd/mm/yyyy")
    

today = date.today()
if byear > today.year:
    print("Year Invalid")

if bmonth < 1 or bmonth > 12:
    print("Month Invalid")

if bdate < 1 or bdate > 31:
    print("Date Invalid")


if bmonth in [4, 6, 9, 11] and bdate > 30:
    print("Date Invalid")

if bmonth == 2:
    if byear % 4 == 0:
        if bdate > 29:
            print("Date Invalid")
    else:
        if bdate > 28:
            print("Date Invalid")

age = today.year - byear

if (today.month, today.day) < (bmonth, bdate):
    age -= 1

print("Your age is:", age)
