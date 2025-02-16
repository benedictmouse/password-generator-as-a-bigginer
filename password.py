import random


PASS=  "qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM1234567890!@#$%^&*()_"

while True:
    try:
        length = int(input("please seletc the size of the pass"))
        if length <=8:
            print("password must be at least 8 characters long")
            continue
        
        password = ''.join(random.sample(PASS,length))
        print(password)
        break
    except ValueError:
        print("please enter a valis value")