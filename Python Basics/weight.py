weight = float(input("Enter the weight: "))
unit = input("Enter the unit (lbs or kg): ").lower()

if unit == "lbs":
    converted_weight = weight * 2 
    print(f"{weight} lbs is equal to {converted_weight:.2f} kg.")
else:
    converted_weight = weight / 2 
    print(f"{weight} kg is equal to {converted_weight:.2f} lbs.")