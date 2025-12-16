print("Welcome to the Physics Calculator", "Please enter your values")
distance = float(input("Enter the distance in m: "))
velocity = float(input("Enter the velocity in m/s: "))
mass = float(input("Enter the mass in kg: "))
acceleration = float(input("Enter the acceleration in m/s: "))
acceleration_due_to_gravity = float(input("Enter the acceleration due to gravity in m/s^2: "))
height = float(input("Enter the height in m: "))
force = float(input("Enter the force in N: "))
area = float(input("Enter the area of the surface in m^2: "))
volume = float(input("Enter the volume of the surface in m^3: "))

formula_1 = Force = mass *acceleration
formula_2 = work_done = force * distance
formula_3 = weight = mass * acceleration_due_to_gravity
formula_4 = density = mass / volume
formula_5 = pressure = force / area

a = formula_1
b = formula_2
c = formula_3
d = formula_4
e = formula_5
choice = input('What formula would you like to use (choose from "a" to "e")')
if choice == 'a':
    print(a)
elif choice == 'b':
    print(b)
elif choice == 'c':
    print('the answer is ', c)
else :
    print("Please enter a valid choice")


