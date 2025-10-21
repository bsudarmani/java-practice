class Test:
    age = 20
    def __init__(self):
        print(self.age)
    @classmethod
    def print(cls):
        cls.name = "Munees"
        print(cls.age)
        print(cls.name)
    @staticmethod
    def dis():
        name = "waran"
        print(name)

t = Test()
print(t.age)
Test.print()
Test.dis()
