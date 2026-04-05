# todo: add checks for doors and roof constraints
class Vehicle:
    vehicle_type = ""

class Automobile(Vehicle):
    year = "" # year will not be used in math, so I chose to use a string
    make = ""
    model = ""
    doors = "" # 2 or 4. also a string; will not be used in math
    valid_doors = ("2", "4")
    roof = "" # solid or sun roof
    valid_roof = ("solid", "sun roof")

print("Hello. Please give me some details about a car to test my Automobile class.")
Vehicle.vehicle_type = "car"
# The assignment says "Write an app that will accept user input for a car. 
# The app will store 'car' into the vehicle type in your Vehicle super class. "
# I took this to mean that this particular app is only for a car, even though the class has the Vehicle Type variable.
# That's why the program puts in the vehicle type itself, rather than taking the user's input.

user_car = Automobile()
user_car.year = input("What year was the car made? ")
user_car.make = input("What make is the car? (e.g. Toyota, Ford) ")
user_car.model = input("What model is the car? (e.g. Corolla, Mustang) ")

while user_car.doors not in user_car.valid_doors:
    user_car.doors = input("How many doors does the car have? (Enter 2 or 4) ").strip()
    if user_car.doors not in user_car.valid_doors:
        print("Please input a valid number (2 or 4).")

while user_car.roof not in user_car.valid_roof:
    user_car.roof = input("What type of roof does the car have? (Enter solid or sun roof) ").strip().lower()
    if user_car.roof not in user_car.valid_roof:
        print("Please input a valid roof (solid or sun roof)") # I would probably change this 
                                                               # to use Automobile.valid_roof in case more types of roofs 
                                                               # are added later in a real program. Same with the valid_doors one above.

print()
print(f"Vehicle type: {user_car.vehicle_type}")
print(f"Year: {user_car.year}")
print(f"Make: {user_car.make}")
print(f"Model: {user_car.model}")
print(f"Number of doors: {user_car.doors}")
print(f"Type of roof: {user_car.roof}")