import random
import time

a="abcdefghijklmnopqrstuvwxyz"
b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c="0123456789"
d="!@&+_-*"

n=int(input("Введите количество символов пароля: "))
all = a + b + c + d
password = "".join(random. sample(all,n))
print("Идет генерация пароля...")
time.sleep(2)
print("Забирай пароль: ")
print(password)
input()