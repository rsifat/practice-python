class A:
    def feature_1 (self):
        print("this is feature 1")

    def feature_2 (self):
        print("this is feature 2")

#single level inheritance

class B:
    def feature3(self):
        print("this is feature 3")
    def feature4(self):
        print("this is feature 4")

#Multiple leavel Inheritance
class C(A,B):
    def feature5(self):
        print("this is feature 1")

a1=A()
b1=B()
c1=C()

c1.feature_2()

print(c1)