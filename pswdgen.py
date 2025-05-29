import string
import random
import pyperclip as pc
from enum import Enum
import os.path

# string.ascii_letters = abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# string.digits = 0123456789
# string.punctuation = !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~

# DATA DEFINITIONS
# Password Option is one of:
#   - ASCII
#   - DIGIT 
#   - PUNCT
# interp. a password option that could be one of these three 

# None -> Natural
# produces a natural given the user input
def getPasswordLength():
    while True:
        try:
            userInput = int(input("How long you want your password?: "))
            if userInput > 0:
                return userInput
            else:
                print("Invalid, enter a number greater than 0")
        except ValueError:
            print("Invalid, please try again")

# None -> Boolean
# produces true if the user input 'yes' or 'y', 
#          false if the user input 'no' or 'n',
#          repeat asking otherwise
def askYesNo(prompt):
    while True:
        userInput = input(prompt).lower()
        if userInput == "yes" or userInput == "y" or userInput == '':
            return True
        elif userInput == "no" or userInput == "n":
            return False
        else:
            print("Invalid option, try again")


# None -> listof_PasswordOption
# produces a 3 elements long list of PasswordOption given by the user 
def getUserChoice():
    options = []

    if askYesNo("Include ASCII? (Y/n): "):
        options.append("ASCII")
    
    if askYesNo("Include numbers? (Y/n): "):
        options.append("DIGIT")

    if askYesNo("Include punctuation? (Y/n): "):
        options.append("PUNCT")

    return options 



# listOf_PasswordOption Natural -> String
# produces a random password given the character pool and 
#          length of the wanted password
def genRandomPassword(pOptions, length):
    characterPool = ""
    for opt in pOptions:
        match opt:
            case "ASCII":
                characterPool += string.ascii_letters
            case "DIGIT":
                characterPool += string.digits
            case "PUNCT":
                characterPool += string.punctuation

    result = ""
    for _ in range(length):
        result += random.choice(characterPool)
    
    return result

def getWebsite():
    website_url = input("Which website this password is for? ")
    return website_url

def savePasswordToTxt(password):
    if askYesNo("Do you want to save this new password? (Y/n): "):
        website = getWebsite()
        # Save to Scripts/saved_password.txt
        save_path = os.path.abspath('Scripts')
        file = open(os.path.join(save_path, "saved_password.txt"), 'a')
        file.write(f"URL: {website}, PASSWORD: {password}\n")
        file.close()
        print('Saved...')

def main():
    password = genRandomPassword(getUserChoice(), getPasswordLength())
    savePasswordToTxt(password)
    pc.copy(password)
    print(f"Password generated: {password}\nCopied to your clipboard")

if __name__=="__main__":
    main()
