import string, random

char = string.punctuation + string.ascii_letters + string.digits
pwd = ''
lenght = int(input('Enter the lenght of your password: '))

def passwords(userIn, chars, store_pass):
    for i in range(userIn):
        store_pass += random.choice(chars)
    return store_pass

print(passwords(lenght, char, pwd))