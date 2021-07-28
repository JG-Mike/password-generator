import random
import string

# length of password 
length = int(input('\nEnter the length of password: ')) 

# define characters for making password
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

# use random
temp = random.sample(all,length)

# create the password
password = "".join(temp)

# print the password madetf
print(password)

