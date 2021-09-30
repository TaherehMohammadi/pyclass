# Tahereh Mohammadi - Thursday 14-18
# sort the list in accending

# 1st solution: without knowing default letter ranking:
people=['ali','negin','negar','reza','hossein','mehrdad','X']

letter_asc=list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
def sortedlist(mylist :list, l=0):
    sortedlist=list()
    n=0
    while n<len(letter_asc):
        for word in mylist:
            if word[l]==letter_asc[n]:
                sortedlist.append(word)
        n=n+1
    return sortedlist


print('sorted people by 1st solution:\n',sortedlist(people))
print('----------------------------------------------------------------')

# 2nd solution: with knowing default letter ranking:
people=['ali','negin','negar','reza','hossein','mehrdad','X']

def sortedlist(mylist :list):
    m=0
    while m<len(mylist)-1:
        for n in range(0,len(mylist)-1):
            if mylist[n]>mylist[n+1]:
                mylist[n] , mylist[n+1]= mylist[n+1] , mylist[n]
        m=m+1
    return mylist


print('sorted people by 2nd solution:\n',sortedlist(people))
print('----------------------------------------------------------------')
