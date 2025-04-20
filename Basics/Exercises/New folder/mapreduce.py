from functools import reduce

student_data = [
    ("Alice", 500, 450, 90),
    ("Bob", 500, 200, 85),
    ("Charlie", 500, 320, 80),
    ("David", 500, 150, 70),  
    ("Emma", 500, 490, 95)
]

def calculate_result(data):
    name, total_marks, obtained_marks, attendance = data
    percentage = (obtained_marks / total_marks) * 100 
    status = "Pass" if percentage >= 40 and attendance >= 75 else "Fail"  
    return (name, round(percentage, 2), attendance, status) 

results = list(map(calculate_result, student_data))
print("\nStudent Results (Name, Percentage, Attendance, Status):")
for res in results:
    print(res)

def failed_students(data):
    name, total_marks, obtained_marks, attendance = data
    percentage = (obtained_marks / total_marks) * 100
    return percentage < 40 or attendance < 75  

failed_students_list = list(filter(failed_students, student_data))
print("\nFailed Students:", [s[0] for s in failed_students_list])

total_obtained_marks = reduce(lambda acc, data: acc + data[2], student_data, 0)
total_attendance = reduce(lambda acc, data: acc + data[3], student_data, 0)

average_attendance = total_attendance / len(student_data)  

print("\nTotal Marks Obtained by All Students:", total_obtained_marks)
print("Average Attendance of All Students: {:.2f}%".format(average_attendance))


