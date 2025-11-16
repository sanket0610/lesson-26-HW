import random
import string

print("WELCOME TO PASSWORD GENERATOR")
l=int(input("ENTER THE LENGTH OF PASSWORD: "))

lo=string.ascii_lowercase
u=string.ascii_uppercase
n=string.digits
s=string.punctuation
a=lo+u+n+s

temp=random.sample(a,l)
password="".join(temp)
print(password)