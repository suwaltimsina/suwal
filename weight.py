"""converting kilogram to lbs and lbs to km"""
def kg_to_lbs(kg):
    lbs = kg*2.20462
    return lbs

def lbs_to_kg(lbs):
    kg = lbs*0.453592
    return kg

choose = input("enter kg to convert into lbs and lbs to convert into kg: ")

if choose.lower() == 'kg':
    weight_in_kg = float(input("enter weight: "))
    print(f"{weight_in_kg} kg is {kg_to_lbs(weight_in_kg)} lbs.")
elif choose.lower() == 'lbs':
    weight_in_lbs = float(input("enter weight: "))
    print(f"{weight_in_lbs} lbs is {lbs_to_kg(weight_in_lbs)} kg.")