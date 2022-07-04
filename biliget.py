import requests as res
from os import system as cmd
import os
import sys
import wget
from colorama import Fore as cfore

__version__ = '1.3'
__doc__ = """

An tool to download videos form website like bilibili,it depend on tenapi
(https://tenapi.cn).

"""
def cmddl():
    cmdinli = sys.argv[1:]
    dict = {}
    if len(cmdinli) != 0:

        if 'https://' == cmdinli[0][0:8] or 'http://' == cmdinli[0][0:7]:
            dict['url'] = cmdinli[0]
            if '-h' or '--help' in cmdinli:
                print(__version__+__doc__)
                a = 0
        for t in cmdinli:
            a += 1
            if t == '-o':
                try:
                    os.listdir(t)
                except:
                    print(cfore.YELLOW+ "Could not list the output dir" +cfore.RESET)
                else:
                    dict['outdir'] = cmdinli[a]



cmddl()
print(f"Use the ten api(https://tenapi.cn/)\nProgram version:1.3")
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
            sys.exit()
        else:
            print("Wrong!")
            sys.exit()
