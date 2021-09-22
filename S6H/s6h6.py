# Tahereh Mohammadi - Thursday 14-18
# summerize a fenglish sentence

sentence=input('enter a fenglish sentence:\n')
print('==========================')
sentence=sentence.split(' ')

#1st solution:
# sentence=input('enter a fenglish sentence:\n')
# print('==========================')
# sentence=sentence.split(' ')
summerize=list()
n=0
while n<len(sentence):
    word=sentence[n]
    word=word[::2]
    summerize.append(word)
    n=n+1
summerize=' '.join(summerize)
print('output of 1st solution:')
print(summerize)
print('*******************************')

#2nd solution:
# sentence=input('enter a fenglish sentence:\n')
# print('==========================')
# sentence=sentence.split(' ')
summerize=''
for word in sentence:
    word=word[::2]
    summerize=summerize+' '+word
print('output of 2nd solution:')
print(summerize)
print('*******************************')
