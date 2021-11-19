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
    
    # def __add__(self, other):
    #     return self.salary+other.salary

    def __repr__self():
        return 'Employee'


rakin =Employee('rakin', 'hasan', 7500,)
rony =Employee('rony', 'khan', 4500,)


print(repr(rakin))

