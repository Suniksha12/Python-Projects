import os
#inside this shutil we have a move funstion for which they move the file from one location to another
import shutil

path = input("Enter your path : ")

files = os.listdir(path)

for i in files:
    # print(i)
    filename , extension = os.path.splitext(i)
    # print(filename)
    # #after printing the extension it will fetch with . and we need that to be removed
    # print(extension)
    #In the below statemnet we doing slicing of the string
    extension_1 = extension[1:]
    # print(extension_1)
    #with the  help of this extension we will make a folder
    folder_path = path+"\\"+extension_1
    if(os.path.exists(folder_path)):
        # print("True")
        shutil.move(path+"\\"+i,path+"\\"+extension_1+"\\"+i)
    else :
        # print("False")
        os.makedirs(folder_path)
        shutil.move(path+"\\"+i,path+"\\"+extension_1+"\\"+i)

#With the files names fetches we want to seperated the file name and the extension
