height = float(input("Enter your height in inches:"))
weight = float(input("Enter your weight in lbs:"))
bmi = (weight * 703) / (height * height)

if bmi < 16.0:
    print(f"You are severely underweight with a{bmi} bmi")
elif 16.0 <= bmi <= 18.4:
    print(f"You are underweight with a{bmi} bmi")
elif 18.5 <= bmi <= 24.9:
    print(f"You are normal weight with a{bmi} bmi")
elif 25.0 <= bmi <= 29.9:
    print(f"You are overweight with a{bmi} bmi")
elif 30.0 <= bmi <= 34.9:
    print(f"You are moderately obese with a{bmi} bmi")
elif 35.0 <= bmi <= 39.9:
    print(f"You are severely obese with a{bmi} bmi")
else:
    print(f"You are morbidly obese with a{bmi} bmi")