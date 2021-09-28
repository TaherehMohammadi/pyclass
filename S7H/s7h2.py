# Tahereh Mohammadi - Thursday 14-18
# sort the list in accending

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


print(sortedlist(people))
