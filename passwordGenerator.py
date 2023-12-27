
import random
import string

def generate_password(length):
    # Define the characters to use in the password
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation.replace("'", "").replace('"', '')

    # Generate the password by choosing random characters from each group
    password = ''
    for i in range(length):
        if i == 0:
            password += random.choice(letters)
        elif i == 1:
            password += random.choice(digits)
        elif i == 2:
            password += random.choice(punctuation)
            ''' here upto this the password generate according to the serial of those random choice,
             1st letter then digit then punctuation '''
        else:
            password += random.choice(letters + digits + punctuation)
     
    return password

# Prompt the user to specify the length of the password
length = int(input("Enter the length of the password: "))

# Generate and print the password
password = generate_password(length)
print("Your password is:", password)
