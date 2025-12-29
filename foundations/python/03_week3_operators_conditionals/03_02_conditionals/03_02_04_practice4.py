print("Please enter your height and weight.")

height = int(input("Height (cm): "))
weight = int(input("Weight (kg): "))

bmi = weight / (height * height) * 10000

if bmi > 25:
    print("Obese")
else:
    print("Normal")
