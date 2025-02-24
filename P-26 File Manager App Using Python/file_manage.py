import os

path = input("Enter your path : ")

files = os.listdir(path)

for i in files:
    # print(i)
    filename , extension = os.path.splitext(i)
    # print(filename)
    # #after printing the extension it will fetch with . and we need that to be removed
    # print(extension)

#With the files names fetches we want to seperated the file name and the extension
