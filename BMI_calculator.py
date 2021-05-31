print('Metric system selection. If You want imperial metric system press 2. If You want in system SI press 1')
metric_system = int(input())
print('select your weight')
weight = float(input())
print('select your height')
height = float(input())
bmi_si = weight / (height ** 2)
bmi_imperial = (weight*703) / (height ** 2)
def metric_system(bmi_si, bmi_imperial):
	if metric_system < 2:
		return bmi_si
	else:
		return bmi_imperial
print('Your BMI is:' + metric_system(bmi_si, bmi_imperial))
if metric_system(bmi_si, bmi_imperial) <= 15.0:
	print('very severely underweight')
elif metric_system(bmi_si, bmi_imperial) > 15.0 or metric_system(bmi_si, bmi_imperial) < 16.0:
	print('severely underweight')
elif metric_system(bmi_si, bmi_imperial) > 16.1 or metric_system(bmi_si, bmi_imperial) < 18.4:
	print('underweight')
elif metric_system(bmi_si, bmi_imperial) > 18.5 or metric_system(bmi_si, bmi_imperial) < 24.9:
	print('normal weight')
elif metric_system(bmi_si, bmi_imperial) > 25.0 or metric_system(bmi_si, bmi_imperial) < 29.9:
	print('overweight')
elif metric_system(bmi_si, bmi_imperial) > 30.0 or metric_system(bmi_si, bmi_imperial) < 34.9:
	print('moderately obese')
elif metric_system(bmi_si, bmi_imperial) > 35.0 or metric_system(bmi_si, bmi_imperial) < 39.9:
	print('severely obese')
elif metric_system(bmi_si, bmi_imperial) > 40.0:
	print('very severely (or "morbidly") obese')