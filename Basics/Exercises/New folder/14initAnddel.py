class Person:
    def __init__(self,regno, name):
        self.regno = regno
        self.name = name
        print(f"{self.name} ({self.regno}) has been created.")

    def display(self):
        print(f"Name: {self.name}, RegNo: {self.regno}")

    def __del__(self):
        print(f"{self.name} is being deleted.")


p1 = Person("22us","Raja")
p1.display()

del p1
print("Program Finished")

