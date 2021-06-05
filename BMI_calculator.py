print('Metric system selection. If You want imperial metric system press 2. If You want in system SI press 1')
metric_system = int(input())
print('select your weight')
weight = float(input())
print('select your height')
height = float(input())
def bmi_formula(metric_system, weight, height):
	bmi = metric_system
	bmi_si = weight / (height ** 2)
	bmi_i = (weight*703) / (height ** 2)
	if bmi == 1:
		return bmi_si
	if bmi == 2:
		return bmi_i
bmi_a = bmi_formula(metric_system, weight, height)
print('Your BMI is: ')
print(bmi_a)
if bmi_a < 15.0:
	print('very severely underweight')
elif bmi_a >= 15.0 and bmi_a <= 16.0:
	print('severely underweight')
elif bmi_a >= 16.1 and bmi_a <= 18.4:
	print('underweight')
elif bmi_a >= 18.5 and bmi_a <= 24.9:
	print('normal weight')
elif bmi_a >= 25.0 and bmi_a <= 29.9:
	print('overweight')
elif bmi_a >= 30.0 and bmi_a <= 34.9:
	print('moderately obese')
elif bmi_a >= 35.0 and bmi_a <= 39.9:
	print('severely obese')
elif bmi_a >= 40.0:
	print('very severely (or "morbidly") obese')