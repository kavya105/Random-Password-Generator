import random
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*_"
while True:
    pass_length = int(input("Enter the length of the required password: "))

    pass_count = int(input("Enter the number of required passwords: "))
    for i in range(0 , pass_count):
        password = ""
        for j in range(0 , pass_length):
            pass_character = random.choice(characters)
            password = password+pass_character
        print("The generated password is " , password) 
    repeat = input("Do you want to generate more passwords? ")
    if repeat=="no" or repeat=="No":
        break
print("Thnak you")
