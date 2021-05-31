print('Metric system selection. If You want imperial metric system press 1 in system SI press 2')
metric_system = input()
print('select your weight')
weight = float(input())
print('select your height')
height = float(input())
bmi_si = weight / (height ** 2)
bmi_imperial = (weight*703) / (height ** 2)
def bmi_formula(**bmi_metric):
	bmi_metric = metric_system
	if bmi_metric = 2:
		print(bmi_si)
	else
		print(bmi_imperial)
if bmi_formula <= 15.0:
	print('very severely underweight')
elif bmi_formula > 15.0 or bmi_formula < 16.0:
	print('severely underweight')
elif bmi_formula > 16.1 or bmi_formula < 18.4:
	print('underweight')
elif bmi_formula > 18.5 or bmi_formula < 24.9:
	print('normal weight')
elif bmi_formula > 25.0 or bmi_formula < 29.9:
	print('overweight')
elif bmi_formula > 30.0 or bmi_formula < 34.9:
	print('moderately obese')
elif bmi_formula > 35.0 or bmi_formula < 39.9:
	print('severely obese')
elif bmi_formula > 40.0:
	print('very severely (or "morbidly") obese')
print('Your BMI is:' + bmi_formula())