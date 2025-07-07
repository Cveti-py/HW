weight_kg = 67
height_cm = 170

height_m = height_cm / 100

bmi = weight_kg / (height_m ** 2)

bmi_rounded = round(bmi, 2)

print(f"Your BMI is: {bmi_rounded}")

