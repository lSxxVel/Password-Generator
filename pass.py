import string, random

char = string.punctuation + string.ascii_letters + string.digits

pwd = ''

lenght = int(input('Enter the lenght of your password: '))

for i in range(lenght):
    pwd += random.choice(char)

print(pwd)