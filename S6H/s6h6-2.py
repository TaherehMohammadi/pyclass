# Tahereh Mohammadi - Thursday 14-18
# summerize a fenglish sentence

# sentence=input('enter a fenglish sentence:\n')
# print('==========================')
# voveles=['a','e','i','o','u']
# for char in sentence:
#     if char in voveles:
# sentence=sentence.replace(char,'')
# print(sentence)
############################################
# mylist=['mina','ali']
# name='mina'
# mylist.pop(0)
# print(mylist)
# print('====================')
# mylist=['mina','ali']
# mylist.remove(name)
# print(mylist)
# print('====================')
# mylist=['mina','ali']
# del mylist[0]
# print(mylist)
# print('====================')
###########################################
# sentence='salam reza'
# sentence=sentence.replace('a','')
# print(sentence)
############################################
sentence=input('enter a fenglish sentence:\n')
sentence=sentence.split(' ')
print('==========================')
sentence_new=''
for word in sentence:
    word=word[::2]
    sentence_new=sentence_new+' '+word
print(sentence_new)
