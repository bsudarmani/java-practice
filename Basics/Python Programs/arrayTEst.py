class Student:
    def getData(self,n):
        self.name = input("Enter student name:")
        self.m = [0] * n
        for i in range(n):
            self.m[i] = int(input(f"Enter mark {i+1}:"))
    def findTotal(self):
        self.total  = 0
        for i in self.m:
            self.total+=i
    def avg(self):
        self.avg = self.total / len(self.m)
    def putData(self,sno):
        print(sno,self.name,self.m,self.total,self.avg)


print("\tSTUDENT DETAILS")
n = int(input("Enter number of students:"))
m = int(input("Enter number of marks:"))
s = [Student()] * n
for i in range(n):
    print(f"\tSTUDENT {i+1} DETAILS")
    s[i] = Student()
    s[i].getData(m)
    s[i].findTotal()
    s[i].avg()
    
for i in range(n):
    s[i].putData(i+1)
