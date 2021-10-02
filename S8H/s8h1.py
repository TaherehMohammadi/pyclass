# Tahereh Mohammadi - Thursday 14-18
# insert data in 3 lists to a data base by for loop
# while loop was done and comment now

names = 'ali sara negar hadi mohsen'.split(' ')
ages = [11, 22, 33, 44, 55]
kelasha = ['Python', 'Python', 'Python', 'Data Science', 'Data Science']

import sqlite3
con = sqlite3.connect('G:\\Training\\Python training course\\Data Bases\\mydb.db')
cur = con.cursor()

for n in range(0,len(names)):
# n=0
# while n<len(names):
    cur.execute(f' insert into students (name , age , class)\
                   values ("{names[n]}" , {ages[n]} , "{kelasha[n]}")  ')
    # n=n+1
con.commit()
con.close()
