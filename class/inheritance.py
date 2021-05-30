class A:
    def feature1(self):
        print("F 1 is working")
    def feature2(self):
        print("f 2 working")

class B(A):
    def feature3(self):
        print("F 3 is working")

    def feature4(self):
        print("F 4 is working")

a = A()
a.feature1()

b = B()
b.feature3()
b.feature2()