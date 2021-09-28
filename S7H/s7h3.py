# Tahereh Mohammadi - Thursday 14-18
# calcute the number index of Fibonacci sequence

n=int(input('enter the number:\n'))
while n<=0:
    print(' --------------------------------')
    print('|enter a positive integer number.|') 
    print(' --------------------------------')
    n=int(input('enter the number:\n'))
print(' ---------------------')

print('aswer by loop:')
fb=1
if n==1 or n==2:
    print(f'f({n})={fb}')
elif n>2:
    fbp=fb
    for n in range(3,n+1):
        fb=fb+fbp
        fbp=fb-fbp
    print(f'f({n})={fb}')
print('----------------------')

print('aswer by recursive function:')
def Fibonacci(n):
    fb=1
    if n==1 or n==2:
        print(f'f({n})={fb}')
    elif n>2:
        fbp=1
        fb=Fibonacci(n-1)+Fibonacci(n-2)
print(f'f({n})={fb}')
print('----------------------')
