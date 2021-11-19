class Employee:
    incerment = 1.5

    def __init__(self, fname, lname, salary):
        self.name = fname
        self.lname = lname
        self.salary = salary

    def increase(self):
        self.salary = int(self.salary * self.increment)


    @classmethod
    def change_increment(cls, amount):
        cls.increment = amount


    @classmethod
    def from_str(cls, emp_string):
        fname, lname, salary = emp_string.split("-")
        return cls(fname, lname, salary)


    @staticmethod
    def isopen(day):
        if day == "Friday":
            return False
        else:
            return True


class programmer(Employee):
    def __init__(self, fname, lname, salary, proglang, exp):
        super().__init__(fname, lname, salary)
        self.proglang = proglang
        self.exp = exp
        

    def increase(self):
        self.salary = int(self.salary * (self.increment + 0.7))
        return self.salary
        #print return value of the function , but can not run this program


rakin = programmer('rakin', 'hasan', 7500, 'php', '2 yrs')
#print(rakin.increase())
#print return value of the function , but can not run this program
print(rakin.exp)
print(rakin.salary)



""" rony = Employee('rony', 'khan', 4500)
nitu = Employee.from_str("nitu-A-7000")
rohan = Employee('rohan', 'D', 6500)
print(nitu.salary)
print(Employee.isopen("Friday"))
"""
