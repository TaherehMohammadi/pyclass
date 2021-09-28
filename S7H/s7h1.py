# Tahereh Mohammadi - Thursday 14-18
# calculate n! by recursive function
def factorial(n):
    fa=1
    if n>1:
        fa=n*factorial(n-1)
    return fa

m=int(input('ienter a integer number:'))
print(f'{m}!={factorial(m)}')
