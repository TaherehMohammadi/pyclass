# Tahereh Mohammadi - Thursday 14-18
# sum of even numbers between 1000 to 2000 by for
sum0=0
for n in range(1000,2000):
    if n%2 != 0:
        sum0=sum0+n
        n=n+1
print(sum0)
