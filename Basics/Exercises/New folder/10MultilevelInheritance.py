class Student:
    def __init__(self, name, dob, regno):
        self.name = name
        self.dob = dob
        self.regno = regno

    def display_info(self):
        print(f"Reg No.       : {self.regno}")
        print(f"Student Name  : {self.name}")
        print(f"DOB           : {self.dob}")

class Marks(Student):
    def __init__(self, name, dob, regno, marks):
        super().__init__(name, dob, regno)
        self.marks = marks

    def display_marks(self):
        print("\n" + "-" * 30)
        print(f"{'Subject':<15}{'Marks':>10}")
        print("-" * 30)
        for subject, score in self.marks.items():
            print(f"{subject:<15}{score:>10}")
        print("-" * 30)


class Result(Marks):
    def __init__(self, name, dob, regno, marks):
        super().__init__(name, dob, regno, marks)

    def calculate_total(self):
        return sum(self.marks.values())

    def calculate_percentage(self):
        return self.calculate_total() / len(self.marks)

    def get_grade(self):
        percentage = self.calculate_percentage()
        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "Fail"

    def display_result(self):
        self.display_info()
        self.display_marks()
        print(f"{'Total Marks':<15}{self.calculate_total():>10}")
        print(f"{'Percentage':<15}{self.calculate_percentage():>9.2f}%")
        print(f"{'Grade':<15}{self.get_grade():>10}")
        print("-" * 30)


# Input
regno = input("Enter Reg No.: ")
name = input("Enter Student Name: ")
dob = input("Enter DOB: ")

marks = {}
num_subjects = int(input("Enter number of subjects: "))
for _ in range(num_subjects):
    subject = input("Enter subject name: ")
    score = float(input(f"Enter marks for {subject}: "))
    marks[subject] = score

# Create Result object
student_result = Result(name, dob, regno, marks)
print("\nStudent Result Report:")
student_result.display_result()
    