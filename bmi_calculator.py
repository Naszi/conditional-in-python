height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = round(weight / height ** 2, 2)
if bmi < 18.5:
    print(f"Your BMI index: {bmi}. You are underweight.")
elif bmi < 25:
    print(f"Your BMI index: {bmi}. You are normal weight.")
elif bmi < 30:
    print(f"Your BMI index: {bmi}. You are overweight.")
else:
    print(f"Your BMI index: {bmi}. You are obese.")
