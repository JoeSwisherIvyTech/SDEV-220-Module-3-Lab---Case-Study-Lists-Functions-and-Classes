# todo: add checks for doors and roof constraints
class Vehicle:
    vehicle_type = ""

class Automobile(Vehicle):
    year = "" # year will not be used in math, so I chose to use a string
    make = ""
    model = ""
    doors = "" # 2 or 4. also a string; will not be used in math
    roof = "" # solid or sun roof

print("Hello. Please give me some details about a car to test my Automobile class.")
Vehicle.vehicle_type = "car"

user_car = Automobile()
user_car.year = input("What year was the car made? ")
user_car.make = input("What make is the car? (e.g. Toyota, Ford) ")
user_car.model = input("What model is the car? (e.g. Corolla, Mustang) ")
user_car.doors = input("How many doors does the car have? ")
user_car.roof = input("What type of roof does the car have? (solid or sun roof) ")
print()
print(f"Vehicle type: {user_car.vehicle_type}")
print(f"Year: {user_car.year}")
print(f"Make: {user_car.make}")
print(f"Model: {user_car.model}")
print(f"Number of doors: {user_car.doors}")
print(f"Type of roof: {user_car.roof}")