import random
letters  = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','*','&','(',')','+','-']

print("Password Generator\n")
numLetters = int(input("How many numbers do you want in your password?\n"))
numNumbers = int(input("How many letters do you want in your password?\n"))
numSymbols = int(input("How many symbols do you want in your password?\n"))

password = []

for i in range(1,numLetters+1):
    char = random.choice(letters)
    password += char

for i in range(1,numSymbols+1):
    char = random.choice(symbols)
    password += char

for i in range(1,numNumbers+1):
    char = random.choice(numbers)
    password += char

random.shuffle(password)

password_string = ""
for char in password:
    password_string = password_string + char

print(password_string)
