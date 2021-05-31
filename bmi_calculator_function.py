print('select your weight') 
weight = float(input())
print('select your height')
height = float(input())
def bmi_si(bmi):
	bmi = weight / (height ** 2)
	print('Your BMI is: ' + bmi)
bmi_si(bmi)