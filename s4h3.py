#Tahereh Mohammadi - Thursday 14-18
#calculate mathematical identities(ettehad_ha)
def morabba_sum_2_jomle(a,b):
    '''
    (a+b)**2==a**2+2*a*b+b**2
    '''
    result=a**2+2*a*b+b**2
    return result

def morabba_minus_2_jomle(a,b):
    '''
    (a-b)**2==a**2-2*a*b+b**2
    '''
    result=a**2-2*a*b+b**2
    return result

def mozdavaj(a,b):
    '''
    a**2-b**2==(a+b)(a-b)
    '''
    result=(a+b)*(a-b)
    return result

def mokkab_sum_2_jomle(a,b):
    '''
    (a+b)**3==a**3+3*a**2*b+3*a*b**2+b**3
    '''
    result=a**3+3*a**2*b+3*a*b**2+b**3
    return result

def mokkab_minus_2_jomle(a,b):
    '''
    (a-b)**3==a**3-3*a**2*b+3*a*b**2-b**3
    '''
    result=a**3-3*a**2*b+3*a*b**2-b**3
    return result

ettehad=int(input('enter the number of the identity that you want?\n\
1-morabba_sum_2_jomle\n\
2-morabba_minus_2_jomle\n\
3-mozdavaj\n\
4-mokkab_sum_2_jomle\n\
5-mokkab_minus_2_jomle\n\n'))
if ettehad>5:
    print('you entered the wrong number for selectting the ettehad')
else:
    a=float(input('enter the first no:\n'))
    b=float(input('enter the second no:\n'))
    if ettehad==1:
        print(f'\n({a}+{b})**2={round(morabba_sum_2_jomle(a,b),2)}')
    elif ettehad==2:
        print(f'\n({a}-{b})**2={round(morabba_minus_2_jomle(a,b),2)}')
    elif ettehad==3:
        print(f'\n{a}**2-{b}**2={round(mozdavaj(a,b),2)}')
    elif  ettehad==4:
        print(f'({a}-{b})**3={round(mokkab_sum_2_jomle(a,b),2)}')
    elif ettehad==5:
        print(f'({a}-{b})**3={round(mokkab_minus_2_jomle(a,b),2)}')
