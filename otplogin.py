import random

otpgenerator = random.randint(000000,100000)
username=input("Username: ")
print("Hello!", username)
print("Here is your otp for login", otpgenerator)

PSWD = input("Enter the otp to login: ")
if PSWD==str(otpgenerator):
    print("Successfully Login!")
else:
    PSWD !=str(otpgenerator)
    print("Failed to login")