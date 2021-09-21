# Tahereh Mohammadi - Thursday 14-18
# calculate mean of numbers that the user entered those

numbers=input('entered numbers(seperate the numbers by ,):\n')
numbers=numbers.split(',')
n=0
sum0=0
while n<len(numbers):
    sum0=sum0+int(numbers[n])
    n=n+1
print('===============================')
print(f'mean={round(sum0/len(numbers),2)}')
