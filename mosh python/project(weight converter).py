#jjunsheng's solution
weight = input("Weight : ")
lbs_or_kg = input("(L)bs or (K)g : ")
if 'l' in lbs_or_kg.lower():
    weight_pounds = int(weight) * 0.45
    print(f"You are {weight_pounds} pounds.")
elif 'k' in lbs_or_kg.lower():
    weight_kilo = int(weight) * 2.25
    print(f"You are {weight_kilo} kilos.")

#mosh solution
weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight // 0.45
    print(f"You are {converted} pounds")