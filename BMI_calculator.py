print('Metric system selection. If You want imperial metric system press 2. If You want in system SI press 1')
metric_system = int(input())
print('select your weight')
weight = float(input())
print('select your height')
height = float(input())
def bmi_formula(w, h, m, bmi_si, bmi_i):
	m = metric_system
	w = weight
	h = height
	bmi_si = w / (h ** 2)
	bmi_i = (w*703) / (h ** 2)
	if m == 1:
		return bmi_si
	if m == 2:
		return bmi_i
bmi_formula(w, h, m, bmi_si, bmi_i)