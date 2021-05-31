print('select your weight') 
weight = float(input())
print('select your height')
height = float(input())
def bmi_si(**bmi):
	bmi = weight / (height ** 2)
	print(bmi)
bmi_si('Your BMI is: ' + bmi)