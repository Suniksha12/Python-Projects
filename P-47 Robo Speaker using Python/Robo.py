import os

if __name__ == '__main__':
    print("Welcome to Robo Speaker 1.1 Created by Whossh-tech")
    x = input("Enter What do you want me to speak: ")
    command = f"say {x}"
    os.system(command)