#BUILDING A PASSWORD GENERATOR IN 2 WAYS
# print("You are welcome to a password hgeneartor app")
import random
from secrets import choice
numbers="0123456789"
symbols="/.,;[]&*%$#@!"
letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
nr_symbols=int(input("How many symbols would you like to make your password consist?\n"))
nr_letters=int(input("how any letters?\n"))
nr_numbers=int(input("How many numbers?\n"))
password=[]
for char in range(nr_letters+1):
    randed_pass=random.choice(letters)
    # password.append(randed_pass)
    # print(randed_pass)
for char in range(1,nr_numbers+1):
    randed_pass=random.choice(numbers)
    # randed_pass=random.choice(numbers)
    password.append(randed_pass)
for char in range(1,nr_symbols+1):
    randed_pass=random.choice(symbols)
    password.append(randed_pass)
    random.shuffle(password)
password_changed=""
for char in password:
    password_changed+=char

print(f"Your  first password is {password_changed}")


# ANOTHER FAST METHOD OF GENRATINF PASSWORD IS
# import random
letter="QWEERTTYUIOPLKJHGFDSAZXCVBNM"
numbers="0123456789"
symbols="{}()/.,?><;'\][]"
all=letter+numbers+symbols
lenght=int(input("Your  second password should be how much lenght?\n"))
password="".join(random.sample(all,lenght))
print(f"Your second password is {password}")     

    
