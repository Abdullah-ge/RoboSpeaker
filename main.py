import os


# For Macbook users; it is simple to give command as "say" but for windows
# you need to attach a VBScript file and give a command


if __name__ == '__main__':
    print("Welcome to Text to speak 1.1 ; Created by Abdullah Sarfraz Ali")

    while True:
        x = input("Enter what you want me to speak : ")
        y = "Ok Bye Bye"
        if x == "s":
            command = f"echo {y} | powershell -ExecutionPolicy Bypass -File text2speak.ps1"
            os.system(command)
            break
        command = f"echo {x} | powershell -ExecutionPolicy Bypass -File text2speak.ps1"
        os.system(command)

