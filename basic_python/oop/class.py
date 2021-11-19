class Employee:
    def __init__(self,fname,lname,salary) -> None:
        self.fname = fname
        self.lname = lname
        self.salary = salary


rony = Employee("rony",'K',4400)
rohan = Employee('rohan','D',4000)


print(rony.salary,rony.fname+rony.lname)
print(rohan.salary)