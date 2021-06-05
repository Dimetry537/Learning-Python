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
print ('Your BMI is:')
print(bmi_formula(metric_system, weight, height))
if bmi_formula(metric_system, weight, height) <= 15.0:
	print('very severely underweight')
elif bmi_formula(metric_system, weight, height) >= 15.0 or bmi_formula(metric_system, weight, height) <= 16.0:
	print('severely underweight')
elif bmi_formula(metric_system, weight, height) >= 16.1 or bmi_formula(metric_system, weight, height) <= 18.4:
	print('underweight')
elif bmi_formula(metric_system, weight, height) >= 18.5 or bmi_formula(metric_system, weight, height) <= 24.9:
	print('normal weight')
elif bmi_formula(metric_system, weight, height) >= 25.0 or bmi_formula(metric_system, weight, height) <= 29.9:
	print('overweight')
elif bmi_formula(metric_system, weight, height) >= 30.0 or bmi_formula(metric_system, weight, height) <= 34.9:
	print('moderately obese')
elif bmi_formula(metric_system, weight, height) >= 35.0 or bmi_formula(metric_system, weight, height) <= 39.9:
	print('severely obese')
elif bmi_formula(metric_system, weight, height) >= 40.0:
	print('very severely (or "morbidly") obese')