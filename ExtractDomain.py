#Created by : t.me/awsi5

import os

print('Put your emails in "Emails.txt"')
print('do not put the "@" sign')

def Extracting(Domain):
    try:
        file_check = os.stat("Emails.txt").st_size == 0
        if file_check == True:
            print('The file is empty')
        else:
            try:
                print('starting...')
                file = open('Emails.txt', 'r').read().splitlines()
                for account in file:
                    if len(account.split()) == 0:
                        pass
                    else:
                        email = account.split('@')[1]
                        if email == Domain:
                            try:
                                a = account.split(':')[1]
                                with open(f'{Domain}.txt', 'a') as save:
                                    save.write(f"{''.join(a.split())}\n")

                            except:
                                with open(f'{Domain}.txt', 'a') as save:
                                    save.write(f"{''.join(account.split())}\n")

            except:
                pass
    except:
        print("Error, make sure: - Install Python, put the emails in a file 'Emails.txt'")

Domain = input('type the Domain : ')
Extracting(Domain)
input('Press Enter to exit : ')
