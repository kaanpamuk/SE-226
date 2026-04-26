class Vehicle:
    def __init__(self, vid, model, year):
        self.vid = vid
        self.model = model
        self.year = year

    def __str__(self):
        return self.vid + " " + self.model + " " + str(self.year)

    def __eq__(self, other):
        return self.vid == other.vid

    def is_new(self, n):
        return self.year >= 2026 - n


class Car(Vehicle):
    def __init__(self, vid, model, year, fuel_type, doors):
        Vehicle.__init__(self, vid, model, year)
        self.fuel_type = fuel_type
        self.doors = doors

    def __str__(self):
        return "Car: " + self.vid + " " + self.model + " " + str(self.year) + " " + self.fuel_type


class Truck(Vehicle):
    def __init__(self, vid, model, year, max_load, axles):
        Vehicle.__init__(self, vid, model, year)
        self.max_load = max_load
        self.axles = axles

    def __str__(self):
        return "Truck: " + self.vid + " " + self.model + " " + str(self.year)


class Motorcycle(Vehicle):
    def __init__(self, vid, model, year, engine_cc, type):
        Vehicle.__init__(self, vid, model, year)
        self.engine_cc = engine_cc
        self.type = type

    def __str__(self):
        return "Motorcycle: " + self.vid + " " + self.model + " " + str(self.year)


def save_fleet_to_file(vehicles, filename):
    file = open(filename, "w")

    for i in range(len(vehicles)):
        v = vehicles[i]

        if type(v) == Car:
            file.write("Car," + v.vid + "," + v.model + "," + str(v.year) + "," + v.fuel_type + "," + str(v.doors) + "\n")

        elif type(v) == Truck:
            file.write("Truck," + v.vid + "," + v.model + "," + str(v.year) + "," + str(v.max_load) + "," + str(v.axles) + "\n")

        elif type(v) == Motorcycle:
            file.write("Motorcycle," + v.vid + "," + v.model + "," + str(v.year) + "," + str(v.engine_cc) + "," + v.type + "\n")

    file.close()


def load_fleet_from_file(filename):
    vehicles = []
    file = open(filename, "r")

    for line in file:
        parts = line.strip().split(",")

        if parts[0] == "Car":
            a = Car(parts[1], parts[2], int(parts[3]), parts[4], int(parts[5]))

        elif parts[0] == "Truck":
            a = Truck(parts[1], parts[2], int(parts[3]), int(parts[4]), int(parts[5]))

        elif parts[0] == "Motorcycle":
            a = Motorcycle(parts[1], parts[2], int(parts[3]), int(parts[4]), parts[5])

        vehicles.append(a)

    file.close()
    return vehicles





v1 = Car("V001", "Tesla", 2023, "Electric", 4)
v2 = Car("V002", "Toyota", 2018, "Petrol", 4)

v3 = Truck("T001", "Volvo", 2021, 20000, 6)
v4 = Truck("T002", "Mercedes", 2019, 18000, 4)

v5 = Motorcycle("M001", "Yamaha", 2024, 1000, "Sport")
v6 = Motorcycle("M002", "Harley", 2015, 1200, "Cruiser")

vehicles = [v1, v2, v3, v4, v5, v6]

save_fleet_to_file(vehicles, "fleet.txt")

loaded = load_fleet_from_file("fleet.txt")

print("All Vehicles")
for i in range(len(loaded)):
    print(loaded[i])

print("Recent Vehicles")
for i in range(len(loaded)):
    if loaded[i].is_new(4):


        print(loaded[i])

print("Electric Cars")
for i in range(len(loaded)):
    if type(loaded[i]) == Car:

        if loaded[i].fuel_type == "Electric":
            print(loaded[i])