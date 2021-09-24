#Tahereh Mohammadi - Thursday 14-18
#calculate BMI with function
def bmi(height,wieght):
#weight in kg & height in cm
    bmi=wieght/((height/100)**2)
    print(f'BMI={bmi}')
    if bmi<=18.5:
        print('you have under weight.')
    elif bmi>18.5 and bmi<=24.9:
        print('you have normal weight.')
    elif bmi >=25 and bmi<=29.9:
        print('you have over weight.')
    else:
        print('you have obesity.')

bmi(163,68)
bmi(173,50)
bmi(165,55)
bmi(155,90)
