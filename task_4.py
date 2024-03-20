import csv
import random

def generate_login(name):
    name = name.split(' ')
    login = f'{name[0]}_{name[1][0]}{name[2][0]}'
    return login

def generate_password():
    characters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789'
    password = ''.join(random.choice(characters) for i in range(10))
    return password

with open('scientist.txt', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter='#'))
    for row in reader:
        login = generate_login(row['ScientistName'])
        password = generate_password()
        row['login'] = login
        row['password'] = password

with open('scientist_password.csv', 'w', encoding='utf-8', newline='') as file:
    fieldnames = list(reader[0].keys())
    w = csv.DictWriter(file, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(reader)