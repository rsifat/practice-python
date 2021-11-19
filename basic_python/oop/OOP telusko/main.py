class computer:
    def __init__(self):
        self.name = "name"
        self.age = "age"

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = computer()
c2 = computer()

c1.age = 40

if c1.compare(c2):
    print("They are same")
else:
    print("they are not same")

print(c1.name)
print(c1.age)
