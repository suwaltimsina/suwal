"""code to convert miles into km and kn into miles."""
def miles_to_kilometers(miles):
    km = miles*1.60934
    return km

def kilometers_to_miles(kilometers):
    miles = kilometers*0.621371
    return miles
"""letting the user choose what he/she want to convert"""
miles_or_km = input("enter km to convert to miles or enter miles to convert into km: ")

"""conditional statement that acts as the user input..."""
if miles_or_km.lower() == 'km':
    distance_in_km = float(input("enter km: "))
    print(f"{distance_in_km} kilometer is {kilometers_to_miles(distance_in_km)} miles.")
elif miles_or_km.lower() == 'miles':
    distance_in_miles = float(input("enter miles: "))
    print(f"{distance_in_miles} miles is {miles_to_kilometers(distance_in_miles)} kilometers...")