class Vehicle:
    def __init__(self, registrationNumber, make, model):
        self.registrationNumber = registrationNumber
        self.make = make
        self.model = model

    def displayInfo(self):
        return f"\nRegistration Number: {self.registrationNumber}, \nMake: {self.make}, \nModel: {self.model}"

class Car(Vehicle):
    def __init__(self, registrationNumber, make, model, numberOfSeats):
        super().__init__(registrationNumber, make, model)
        self.numberOfSeats = numberOfSeats

    def displayInfo(self):
        return f"{super().displayInfo()}, \nNumber of Seats: {self.numberOfSeats}"

class Truck(Vehicle):
    def __init__(self, registrationNumber, make, model, cargoCapacity):
        super().__init__(registrationNumber, make, model)
        self.cargoCapacity = cargoCapacity

    def displayInfo(self):
        return f"{super().displayInfo()}, \nCargo Capacity: {self.cargoCapacity} tons"

class Motorcycle(Vehicle):
    def __init__(self, registrationNumber, make, model, engineCapacity):
        super().__init__(registrationNumber, make, model)
        self.engineCapacity = engineCapacity

    def displayInfo(self):
        return f"{super().displayInfo()}, \nEngine Capacity: {self.engineCapacity} cc"

class Fleet:
    def __init__(self):
        self.vehicles = []

    def addVehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def displayVehicles(self):
        if not self.vehicles:
            print("There are no vehicles in the fleet.")
        else:
            for vehicle in self.vehicles:
                print(vehicle.displayInfo())

    def searchVehicle(self, registrationNumber):
        for vehicle in self.vehicles:
            if vehicle.registrationNumber.lower() == registrationNumber.lower():
                return vehicle.displayInfo()
        return "The vehicle was not found."


fleet = Fleet()


car = Car("KDC 007F", "Mercedes Benz", "AMG GLE 63", 5)
truck = Truck("KAT 700K", "Ford", "F-150", 10)
motorcycle = Motorcycle("KMFE 456A", "Honda", "CBR500R", 500)

fleet.addVehicle(car)
fleet.addVehicle(truck)
fleet.addVehicle(motorcycle)


print("Displaying all vehicles in the fleet:")
fleet.displayVehicles()


registrationNumber = "KDC 007F"
print(f"\nSearching for vehicle with registration number {registrationNumber}:")
print(fleet.searchVehicle(registrationNumber))
