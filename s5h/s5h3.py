# Tahereh Mohammadi - Thursday 14-18
# count the number of uniqe fruits in the lists
fruit1=input('enter a fruit name:\n')
fruit2=input('enter a fruit name:\n')
fruit3=input('enter a fruit name:\n')
fruit4=input('enter a fruit name:\n')
fruit5=input('enter a fruit name:\n')
fruits=[]
fruits[0:5]=fruit1,fruit2,fruit3,fruit4,fruit5
fruits=set(fruits)
print(f'\nyou entered {len(fruits)} uniqe fruits.')
print(f'they are {fruits}.')
