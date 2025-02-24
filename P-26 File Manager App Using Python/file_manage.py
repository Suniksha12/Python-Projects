import os

path = input("Enter your path : ")

files = os.listdir(path)

for i in files:
    print(i)