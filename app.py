weight = float(input("enter your weight in Kilograms: "))
height = float(input("enter your height in meters"))

if height > 0:
    bmi = weight / (height ** 2)
    print(f"Your BMI is {bmi:.2f}")

    if bmi < 18.5:
        print("Category: Underweight")
    elif 18.5 <= bmi < 24.9:
        print("Category: Normal weight")
    elif 25 <= bmi < 29.9:
        print("Category: Overweight")
    else:
        print("Category: Obesity")
else:
    print("Error: Height cannot be zero or negative. Please enter a valid height.")
