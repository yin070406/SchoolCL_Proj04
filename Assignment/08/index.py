weight = float(input("Weight in Kg: "))
height = float(input("Height in Meters: "))

bmi = weight/(height**2)

if bmi < 18.5:
    print("You are Underweight")
elif bmi <= 25:
    print("You are Normal")
else:
    print("You are Overweight")

print(bmi)