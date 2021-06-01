print('Metric system selection. If You want imperial metric system press 2. If You want in system SI press 1')
metric_system = int(input())
print('select your weight')
weight = float(input())
print('select your height')
height = float(input())
bmi_si = weight / (height ** 2)
bmi_imperial = (weight*703) / (height ** 2)
def bmi_formula(w, h, m):
	m = metric_system
	w = weight
	h = height
	if m == 1:
		print(w / (h ** 2))
	if m == 2:
		print((w*703) / (h ** 2))
bmi_formula('Your BMI is: ' + w, h, m)