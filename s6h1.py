# Tahereh Mohammadi - Thursday 14-18
# Numbers between 0 to 10000 that are divisible by 3
n=0
sum3=0
while n>=0 and n<=1000:
    if n%3==0:
        #print(n)
        sum3=sum3+n
    n=n+1
print(format(sum3,','))
