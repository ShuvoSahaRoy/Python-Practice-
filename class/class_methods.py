class Person:
    count_instance = 0

    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    @classmethod
    def count_instances(cls):
        return f"I have created {cls.count_instance} instances of {cls.__name__} class"


p1 = Person('Shuvo', 'Saha', 24)
p2 = Person('Ashik', 'Dhor', 23)

# print(p1.first_name)

print(Person.count_instances())
