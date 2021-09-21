# Tahereh Mohammadi - Thursday 14-18
# summerize a fenglish sentence

sentence=input('enter a fenglish sentence:\n')
print('==========================')
sentence=sentence.split(' ')
summerize=list()
# print(sentence)
n=0
while n<len(sentence):
    word=sentence[n]
    word=word[::2]
    summerize.append(word)
    n=n+1
summerize=' '.join(summerize)    
print(summerize)
