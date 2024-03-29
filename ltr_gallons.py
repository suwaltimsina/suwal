#converting...
def liter_to_gallons(liter):
    gallon = liter * 0.264172
    return gallon
def gallons_to_liter(gallon):
    liter = gallon * 3.78541
    return liter

while True:
    choice = input("enter liters to convert into gallons and gallons to convert into liters: ")
    if choice == 'liters':
        liters = float(input("enter liters: "))
        print(liter_to_gallons(liters), "gallons")
    elif choice == 'gallons':
        gallons = float(input("enter gallons: "))
        print(gallons_to_liter(gallons), "liters")