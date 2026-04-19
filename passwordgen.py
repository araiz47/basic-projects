import random #random password generator version 1  pretty basic atm 

alphabet = "abcdefghijklmnopqrstuvwxyz0123456789,?!@#$%^&*"
numbers = 0,1,2,3,4,5,6,7,8,9
choices = random.choice(alphabet)

password = ""
length = int(input("Enter a length of choice: "))


for i in range(length):
    password+=(random.choice(alphabet))

print(password)


