print('Metric system selection. If You want imperial metric system press 2. If You want in system SI press 1')
metric_system = int(input())
print('select your weight')
weight = float(input())
print('select your height')
height = float(input())
def bmi_formula(bmi):
	bmi = metric_system
	bmi_si = weight / (height ** 2)
	bmi_i = (weight*703) / (height ** 2)
	if bmi == 1:
		return bmi_si
	if bmi == 2:
		return bmi_i
bmi_formula(bmi)