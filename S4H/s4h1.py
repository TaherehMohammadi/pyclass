# Tahereh Mohammadi - Thursday 14-18
# calculate BMI with function
def bmi(height,wieght):
    bmi=wieght/((height/100)**2)
    return bmi

def interpretation(bmi):
    if bmi<=18.5:
        interpretation='you have under weight.'
    elif bmi>18.5 and bmi<=24.9:
        interpretation='you have normal weight.'
    elif bmi >=25 and bmi<=29.9:
        interpretation='you have over weight.'
    else:
        interpretation='you have obesity.'
    return interpretation


height=float(input('Enter your height in centimeter?\n'))
weight=float(input('Enter your weight in kilogram?\n'))
print(f'\nyour bmi is {round(bmi(height,weight),2)} and\
 {interpretation(bmi(height,weight))}')
