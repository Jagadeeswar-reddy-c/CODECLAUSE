import random
import string

def generate_random_password(length = 0, symbols=None, characters=None, numbers = None):
    if symbols != None :
        symbols =  string.punctuation
    else:
        symbols = ''
    if numbers != None :
        numbers = string.digits
    else:
        numbers = ''
    if characters != None :
        characters = string.ascii_letters
    else:
        characters = ''
    
    characters = characters + numbers + symbols
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

