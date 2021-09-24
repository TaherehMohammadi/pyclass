# Tahereh Mohammadi - Thursday 14-18
# make calculator wiyh function with 3 argumants
def calc(no1,no2,operator):
    if operator=='+':
        result=no1+no2
        print(f'{no1}+{no2}={result}')
    elif operator=='-':
        result=no1-no2
        print(f'{no1}-{no2}={result}')
    elif operator=='*':
        result=no1-no2
        print(f'{no1}*{no2}={result}')
    elif operator=='/' and no2!=0:
        result=no1-no2
        print(f'{no1}/{no2}={result}')
    elif operator=='/' and no2==0:
        result=no1-no2
        print(f'{no1}-{no2}=undefied')

calc(4,0,'/')
calc(4,6,'+')
calc(28,10,'-')
calc(54,32,'/')
calc(12,56,'*')
