class Student:
    school = 'KPHS'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def info(cls):          #if we want to use class variables in a function then it should be class funtion and for that cls keyword
        return cls.school

    @staticmethod
    def staticMethods():
        print("this is a static method")

s1 = Student(66,45,52)
s2 = Student(54,66,84)

print(s1.avg())
print(s2.avg())

print(Student.info())

Student.staticMethods()    #we can use s1.info()
