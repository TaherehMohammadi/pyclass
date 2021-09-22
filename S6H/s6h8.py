# Tahereh Mohammadi - Thursday 14-18
# write every words in the list in vertical by while

names=['ali','reza','sara','hadi','negar','mina']
n=0
while n<len(names):
    name=names[n]
    i=0
    while i<len(name):
        print(name[i])
        i=i+1
    print('--------')
    n=n+1
