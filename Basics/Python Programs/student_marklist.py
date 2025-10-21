# Student Marklist Using Multiple Inheritance (Table Format)
class Student:
    def getDetails(self):
        self.name = input("Enter student name: ")
        self.roll = input("Enter roll number: ")

class Marks:
    def getMarks(self):
        self.sub_count = int(input("Enter number of subjects: "))
        self.marks = []
        for i in range(self.sub_count):
            mark = int(input(f"Enter mark for subject {i+1}: "))
            self.marks.append(mark)

    def calculate(self):
        self.total = sum(self.marks)
        self.average = self.total / self.sub_count
        self.failed_subjects = [i for i, m in enumerate(self.marks) if m < 40]
        if self.failed_subjects:
            self.grade = "Fail"
        else:
            if self.average >= 90:
                self.grade = "A+"
            elif self.average >= 80:
                self.grade = "A"
            elif self.average >= 70:
                self.grade = "B"
            elif self.average >= 60:
                self.grade = "C"
            else:
                self.grade = "D"

class Marklist(Student, Marks):
    def displayRow(self):
        display_marks = []
        for i, m in enumerate(self.marks):
            if m < 40:
                display_marks.append(f"{m}*")
            else:
                display_marks.append(str(m))
        # Return row data
        return [self.name, self.roll] + display_marks + [self.total, f"{self.average:.2f}", self.grade]

def main():
    n = int(input("Enter number of students: "))
    students = []

    for i in range(n):
        print(f"\nEnter details for student {i+1}:")
        s = Marklist()
        s.getDetails()
        s.getMarks()
        s.calculate()
        students.append(s)

    print("\n======= STUDENT MARKLIST =======")
    headers = ["Name", "Roll"]
    max_sub = max(s.sub_count for s in students)
    for i in range(1, max_sub+1):
        headers.append(f"Sub{i}")
    headers += ["Total", "Average", "Grade"]

    print("-" * (len(headers)*12))
    print(" | ".join(f"{h:<10}" for h in headers))
    print("-" * (len(headers)*12))

    for s in students:
        row = s.displayRow()
        while len(row) < len(headers):
            row.insert(2, "-")
        print(" | ".join(f"{str(item):<10}" for item in row))

    print("-" * (len(headers)*12))

main()
