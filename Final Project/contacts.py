# Tahereh Mohammadi - Thursdays 14-18
# Final project: Phone Number Contacts



import sys
import sqlite3
import os
class color:
    blue = '\033[94m'
    white = '\033[97m'
    violet = '\033[95m'
con = sqlite3.connect('G:\\Training\\Python training course\\Data Bases\\contacts.db')

print(color.violet + '''
      ||===================================||
      ||  Welcome to Contact list Program! ||
      ||   Written by : Tahereh Mohammadi  ||
      ||===================================||\n''')


def main_menu():
    m = input(color.white + '\n\
    *******************************************\n\
    * for:                                    *\n\
    *        ADD a new contact; press "A"     *\n\
    *        FIND a contact; press "F"        *\n\
    *        EXIT ; press any key             *\n\
    *******************************************\n\
                        : ').lower()
    if m == 'a' or m == 'f':
        print('\n------------------------------------')
        if m == 'a':
            add_contact()
        elif m == 'f':
            search_contact()

    else:
        sys.exit('''Goodbye!''')

def add_contact():
    cur = con.cursor()
    name = input('\nEnter the new contact name:  ').title()
    phone = input('Enter the new contact\'s phone number:  ')
    print('********************************************\n')

    if name == '' or phone == '':
        print(color.blue + '       ---------------------------------')
        print('       |','You don\'t enter new contact.'.center(30),'|')
        print('       ---------------------------------\n')
        main_menu()
    cur = con.cursor()
    cur.execute('select Name,PhoneNumber from contacts')
    mycontacts = cur.fetchall()

    if (name, phone) in mycontacts:
        print(color.blue + '''
        ----------------------------------
        | your contact is already exist. |
        ----------------------------------\n''')
        main_menu()

    cur.execute(f'insert into contacts\
                         (Name,PhoneNumber)\
                   values("{name}","{phone}") ')

    con.commit()

    cur.execute('select max(id) from contacts')
    maxid = (cur.fetchall()[0])[0]

    cur = con.cursor()
    cur.execute(f'select * from contacts\
                   where Id = {maxid}   ')
    result = cur.fetchall()
    print(color.blue +'  ------------------------------------------------')
    print('  |', f'{(result[0])[1]}: {(result[0])[2]}'.center(44), '|')
    print('  |','successfully is added to contact list.'.center(44),'|')
    print('  ------------------------------------------------')
    main_menu()

def search_contact():
    myname = input('Enter a name you\'d like to find: ').title()
    print('------------------------------------')
    cur = con.cursor()
    searchquery = 'select Name,PhoneNumber from contacts'
    cur.execute(searchquery)

    result = cur.fetchall()
    mynames = list()
    myphones = list()
    for rname in result:
        f0, f1 = rname
        mynames.append(f0)
        myphones.append(f1)
    n = 0
    for i, word in enumerate(mynames):
        if word.find(myname) != -1:
            print(color.blue + '------------------------------------')
            print(color.blue + '|', f'{word}:{myphones[i]}'.center(32), '|' )
        n = n + word.find(myname)
    print(color.blue + '------------------------------------')
    if n == -len(mynames):
        print(color.blue + '|', f'"{myname}"'.center(32), '|')
        print('|', 'isn\'t in the contact list.'.center(32), '|')
        print(color.blue + '------------------------------------')
        main_menu()
    choice = input(color.white + '''
    ===============================
     for Edit contact; press "E"
     for Delete contact; press "D"
     for Exit: press any key
    ===============================
                  : ''').lower()
    if choice == 'e':
        edit_contact()
    elif choice == 'd':
        delete_contact()
    else:
        main_menu()

def delete_contact():
    contact_name = input('''\n\nEnter the name exactly like the contact list:\n ''').title()
    phone_number = input('''Enter the phone number:\n ''')

    cur = con.cursor()
    cur.execute(f'select * from contacts\
                  where Name="{contact_name}" and PhoneNumber="{phone_number}"')
    result = cur.fetchall()

    if len(result) != 1:
        print(color.blue + '   --------------------------------------------')
        print('   |','Wrong contact, Try again.'.center(40),'|')
        print('   --------------------------------------------')
        main_menu()

    else:
        cur = con.cursor()
        cur.execute(f'delete from contacts\
                      where Name="{contact_name}" and PhoneNumber="{phone_number}"')

        con.commit()
        print(color.blue + '  ------------------------------------------------')
        print('  |',f'{(result[0])[1]}: {(result[0])[2]}'.center(44),'|')
        print('  |','successfully is deleted from contact list.'.center(44),'|')
        print('  ------------------------------------------------')
        main_menu()

def edit_contact():
    contact_name = input('''\n\nEnter the name exactly like the contact list:\n ''').title()
    phone_number = input('''Enter the phone number:\n ''')

    cur = con.cursor()
    cur.execute(f'select * from contacts\
                  where Name="{contact_name}" and PhoneNumber="{phone_number}"')
    result = cur.fetchall()

    if len(result) != 1:
        print(color.blue + '   --------------------------------------------')
        print('   |','Wrong contact, Try again.'.center(40),'|')
        print('   --------------------------------------------')
        main_menu()
    else:
        new_contact_name = input('Enter the new Name to change:\n ').title()
        new_phone_number = input('Enter new phone number to change:\n ')
        new_contact = (new_contact_name, new_phone_number)
        if new_contact_name == '' or new_phone_number == '':
            print(color.blue + '       -------------------------------------')
            print('       |','You don\'t enter new contact.'.center(33),'|')
            print('       -------------------------------------\n')
            main_menu()

        cur = con.cursor()
        cur.execute(f'select * from contacts\
                      where Name="{new_contact_name}" and PhoneNumber="{new_phone_number}"')
        new_result = cur.fetchall()

        if new_result != []:
            print(color.blue + '''
        ----------------------------------
        | your contact is already exist. |
        ----------------------------------\n''')
            main_menu()
        else:
            cur = con.cursor()
            cur.execute(f'update contacts\
                          set Name="{new_contact_name}" , PhoneNumber="{new_phone_number}"\
                          where Name="{contact_name}" and PhoneNumber="{phone_number}"')

            con.commit()

            print(color.blue + '  ------------------------------------------------')
            print('  |',f'{(result[0])[1]}: {(result[0])[2]}'.center(44),'|')
            print('  |','successfully is edited to'.center(44),'|')
            print('  |',f'{new_contact[0]}: {new_contact[1]}'.center(44),'|')
            print('  ------------------------------------------------')
            main_menu()

main_menu()

con.close()