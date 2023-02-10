height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

new_height = float(height)
new_weight = int(weight)
height_squared = new_height * new_height

BMI = (new_weight / height_squared)

final_BMI = int(BMI)
if final_BMI < 18.5:
    print(f"your BMI is {final_BMI}, you are underweight.")
elif ((final_BMI > 18.5) and (final_BMI < 25)):
    print(f"your BMI is {final_BMI}, you are of a normal weight ")
elif ((final_BMI > 25) and (final_BMI < 30)):
    print(f"your BMI is {final_BMI}, you are slightly overweight.")
elif ((final_BMI > 30) and (final_BMI < 35)):
    print(f"your BMI is {final_BMI}, your are obese.")
elif final_BMI > 35:
    print(f"your BMI is {final_BMI}, you are clinically obese.")