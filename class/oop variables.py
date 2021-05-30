class Car:

    wheels = 4  #class variable

    def __init__(self):
        self.mil =10        #instance variables
        self.com="BMW"      #instance variables


c1 = Car()
c2 = Car()

c1.mil = 8
c1.wheels = 5

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)
