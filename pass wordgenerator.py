#import library
import random

#define combinations
lowers = 'abcdefghijklmnopqrstuvwxyz'
uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '012345678'
symbols = '!@#$%^&*'

combination = lowers + uppers + numbers + symbols

#fix the length of password
length = int(input())

#generating the password
password = ''.join(random.sample(combination, length))

#here the password you got!
print(password)