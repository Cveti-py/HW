# logical_expressions_and_conditional_statements_tasks.py

# ---------------------------------- Task 1 ---------------------------------- #
""" DESCRIPTION:
    Write a program that takes a number as input and checks if it is positive, negative, or zero.
"""

### Your code here

number = float(input("Enter a number: "))
if number > 0:
    print(f"Number {number} is positive.")
elif number < 0:
    print(f"Number {number} is negative.")
else:
    print("Number is zero.")


### EXPECTED OUTPUT:
# "Enter a number: -2.45"
# "Number -2.45 is negative."


# ---------------------------------- Task 2 ---------------------------------- #
""" DESCRIPTION:
    Write a program to check whether a year input by the user is a leap year or not. Use the rule for Gregorian calendar:
    Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400.
    For example, the years 1700, 1800, and 1900 are not leap years, but the years 1600 and 2000 are.
"""

### Your code here

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not leap year.")

### EXPECTED OUTPUT:
# Enter a year: 2024
# 2024 is a leap year

# Enter a year: 2050
# 2050 is not leap year.


# ---------------------------------- Task 3 ---------------------------------- #
""" DESCRIPTION:
    Develop a simple temperature converter program that converts temperatures from Fahrenheit to Celsius and vice versa based on user choice. Make a user-friendly interface as given in EXPECTED OUTPUT:.

    Temperature conversions use the following formulas:
    Temperature in degrees Fahrenheit (°F) = (Temperature in degrees Celsius (°C) * 9/5) + 32.
    Temperature in degrees Celsius (°C) = (Temperature in degrees Fahrenheit (°F) - 32) * 5/9.
"""

### Your code here

print("********** Fahrenheit/Celsius Converter ***********")
print("# 1 => Convert to Fahrenheit                     #")
print("# 2 => Convert to Celsius                        #")
print("**************************************************")

choice = input("Enter your choice [1/2]: ")

if choice == "1":
    celsius = float(input("Enter temperature in C: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}C = {fahrenheit}F")
elif choice == "2":
    fahrenheit = float(input("Enter temperature in F: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}F = {celsius}C")
else:
    print("Invalid choice.")

### EXPECTED OUTPUT:
# **********Fahrenheit/Celsius Converter ***********
# # 1 => Convert to Fahrenheit                     #
# # 2 => Convert to Celsius                        #
# **************************************************
# Enter your choice [1/2]: 1
# Enter temperature in C: 20
# 20.0C = 68.0F


# ---------------------------------- Task 4 ---------------------------------- #
""" DESCRIPTION:
    Write a Body mass index (BMI) calculator program, which asks the user for:
    weight in kilograms
    height in meters

    Calculate the BMI = W / (H*H)
    where:
    W = weight in kilograms
    H = height in meters

    Display to the user the BMI and basic category, using next table:

    | ------------------------------- | ----------- |
    | category                        | BMI         |
    | ------------------------------- | ----------- |
    | Underweight (Severe thinness)   | < 16.0      |
    | Underweight (Moderate thinness) | 16.0 - 16.9 |
    | Underweight (Mild thinness)     | 17.0 - 18.4 |
    | Normal range                    | 18.5 - 24.9 |
    | Overweight (Pre-obese)          | 25.0 - 29.9 |
    | Obese (Class I)                 | 30.0 - 34.9 |
    | Obese (Class II)                | 35.0 - 39.9 |
    | Obese (Class III)               | ≥ 40.0      |
    | ------------------------------- | ----------- |
"""

### Your code here

weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))

bmi = round(weight / (height ** 2), 2)

if bmi < 16.0:
    category = "Underweight (Severe thinness)"
elif bmi < 17.0:
    category = "Underweight (Moderate thinness)"
elif bmi < 18.5:
    category = "Underweight (Mild thinness)"
elif bmi < 25.0:
    category = "Normal range"
elif bmi < 30.0:
    category = "Overweight (Pre-obese)"
elif bmi < 35.0:
    category = "Obese (Class I)"
elif bmi < 40.0:
    category = "Obese (Class II)"
else:
    category = "Obese (Class III)"

print(f"Your BMI = {bmi}, Category: {category}")

### EXPECTED OUTPUT:
# Enter weight in kilograms: 92
# Enter height in meters: 1.78
# Your BMI = 29.04, Category: Overweight (Pre-obese)

