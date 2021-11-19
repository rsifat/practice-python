class Employee:
    # increment = 1.5
    Num_of_Employee = 0

    def __init__(self, fname, lname, salary) -> None:
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.increment = 2
        Employee.Num_of_Employee += 1

    def increse(self):
        # self.salary = int(self.salary * Employee.increment)
        self.salary = int(self.salary * self.increment)


rony = Employee("rony", 'K', 4400)
rohan = Employee('rohan', 'D', 4000)

print("Before increment: ", rony.salary)
rony.increse()
print("after increment: ", rony.salary)

# print(rony.__dict__)
# print(Employee.__dict__)

print("Number of Employee is :", Employee.Num_of_Employee)
