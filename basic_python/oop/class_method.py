class Employee:

    increment = 1.5
    Num_of_Employee =0

    def __init__(self,fname,lname,salary) -> None:
        self.fname = fname
        self.lname = lname
        self.salary = salary
        #self.increment = 4
      


    def increse(self):
        #self.salary = int(self.salary * Employee.increment)
        self.salary = int(self.salary * self.increment)


    @classmethod
    def change_increment(cls, amount):
        cls.increment = amount


rony = Employee("rony",'K',4400)


print("Before increment: ",rony.salary)
Employee.change_increment(1.7)
rony.increse()
print("after increment: ",rony.salary)
