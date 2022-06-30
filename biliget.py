import requests as res
from os import system as cmd
from sys import exit

print(f"Use the ten api(https://tenapi.cn/)\nProgram version:1.2")
u = input("Video url:\n")
apiurl1 = 'https://tenapi.cn/video/?url=' + u

rg1 = res.get(apiurl1)
vurl = rg1.json()['url']
print("\nVideo url:\n",vurl)

p = input("where to save? here/another(H/a)")
if p == None or p in ["H","h"]:
    cmd(f"wget.exe \"{vurl}\" ")
elif p in ["A","a"]:
    try:
        p = input("Where? :\n")
        cmd(f"wget.exe -o \"{p}\" \"{vurl}\" ")
    except:
        print("Failed to save at that direction.Saving atthere?(Y/n)")
        i = input("\n")
        if i in ["Y","y"]:
            cmd(f"wget.exe \"{vurl}\" ")
        elif i in ["N","n"]:
            exit()
        else:
            print("Wrong!")
            exit()
