# Tahereh Mohammadi - Thursday 14-18
# calculate mean of numbers by 2 functions

def get_numbers():
    numbers=input('enter the numbers;seperate them by space.\n')
    numbers=numbers.split(' ')
    n=0
    while n<len(numbers):
        ni=int(numbers[n])
        numbers[n]=ni
        n=n+1
    return numbers
def calculate_mean():
    numbers=get_numbers()
    sum0=0
    n=0
    while n<len(numbers):
        sum0=sum0+numbers[n]
        n=n+1
    print(f'mean={round((sum0/len(numbers)),2)}')

calculate_mean()
