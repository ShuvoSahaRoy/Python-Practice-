class Person:
    count_instance = 0

    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def from_string(cls, string):
        first, last, age = string.split(',')
        return cls(first, last, age)

    @classmethod
    def count_instances(cls):
        return f"I have created {cls.count_instance} instances of {cls.__name__} class"

    @staticmethod
    def msg():
        print("Hello i m static method")


p1 = Person('Shuvo', 'Saha', 24)
p2 = Person('Ashil', 'Dhor', 23)

p3 = Person.from_string('Joy,Dip,22')
print(p3.first_name)

# print(p1.first_name)

print(Person.count_instances())
Person.msg()
