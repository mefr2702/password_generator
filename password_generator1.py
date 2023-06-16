import random
pass: ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
pass_length = int(input("berapa banyak karakter yang  ingin di gunakan di passwordnya":))

password = ""

for i in range(pass_length):
    password += random.choice(pass)

print(password)