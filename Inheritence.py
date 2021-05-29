class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage = mileage
        self.cost = cost

    def show_vehicle(self):
        print("I am a Vehicle")
        print('Mileage of vehicle is ',self.mileage)
        print('Cost of Vehicle is ',self.cost)

v1 = Vehicle(1200,999)
v1.show_vehicle()
class Car(Vehicle):
    def show_car(self):
        print("I am a Car")
c1 = Car(200,1200)
print (c1.show_vehicle())
print (c1.show_car())