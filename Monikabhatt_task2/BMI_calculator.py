# Oasis Infobyte Internship - Task 2:BMI Calculator
# created by: Monika Bhatt

print("===Welcome to the Oasis Infobyte BMI Calculater===")

try:
    weight = float(input("Enter your weight in kilogram:"))
    height = float(input("Enter your height in meters:"))

    if weight <= 0 or height <= 0:
        print("Error: Weigth and height must be greater then zero.")
    else:
        bmi = weight/(height**2)
        print(f"\nYour calculated BMI is:{bmi:.2f}")

    if bmi < 18.5:
        print("Category:Underweight")
    elif 18.5 <= bmi < 24.9:
        print("Category:Normal weight")
    elif 24.9<=bmi<29.9:
        print("Category:Overweight")
    else:
        print("Category:Obese")
except ValueError:
        print("Error:Please enter numbers only. Letters are not allowed.")
    
print("\nThank you for using the BMI Calculator!") 
