#! python3
# strongPasswordDetection.py - Tests to make sure the password string passed is strong
# A strong password is one that is 8 chars long, has upper and lowercase characters, and at least 1 digit

import re

password = input("Enter your password: ")

passwordRegex = re.compile(r'^(?=.*[A-Z]+)(?=.*[a-z]+)(?=.*\d+).*$')

def passwordTest(userPassword):
    testString = passwordRegex.search(userPassword)
    if testString == None or (len(password) < 8):
        return "Your password is weak, dude."
    else:
        return "Your password is strong, dude."
    
print(passwordTest(password))
