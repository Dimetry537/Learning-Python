print('Metric system selection. If You want imperial metric system press 1 in system SI press 2')
metric_system = input()
print('select your weight')
weight = float(input())
print('select your height')
height = float(input())
bmi_si = weight / (height ** 2)
bmi_imperial = (weight*703) / (height ** 2)
