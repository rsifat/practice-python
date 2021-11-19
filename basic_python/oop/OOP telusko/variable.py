class car:
    #  wheels is class variable
    wheels = 4

    def __init__(self):
        # init er modde ja thakbe oi ta e instance variable
        self.name = "Name"
        self.mil = "Mil"


car1 = car()
car2 = car()

car1.name = "BMW"
car1.mil = 22

car2.name = "Audi"
car2.mil = 20

car.wheels = 6

print(car1.name, car1.mil, car1.wheels)
print(car2.name, car2.mil, car2.wheels)
