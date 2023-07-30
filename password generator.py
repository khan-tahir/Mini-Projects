import string
import random

length = int(input("Enter the length of Password : "))
alp = string.ascii_letters
num = string.digits
spec = string.punctuation

all = alp + num + spec

generate_pass = random.sample(all,length)
password = "".join(generate_pass)
print(f"Your generated passwword is {password}")