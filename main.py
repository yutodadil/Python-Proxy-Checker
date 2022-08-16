import random
import string
import pathlib
import requests, os, threading, sys, time, random, ctypes, webbrowser,re, hashlib, datetime, os.path, httpx, sys, gratient
import colorama
from colorama import Fore, init, Back, Style
from datetime import date
import random
from threading import active_count, Thread
import itertools
from colorama import Fore as f

__proxies__ = itertools.cycle(open('./proxies.txt', 'r+').read().splitlines())

def gen():
    auau = next(__proxies__)
    if auau == "null:null":
        text = "End of Check."
        gratient_text = gratient.blue(text)
        print(gratient_text)
        os._exit(1)
    else:
        os.system(f"title Bruter is Now Working. Checking for - {auau}")
        Header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", "accept-language": "ja,en-US;q=0.9,en;q=0.8"}
        req = requests.get(f'https://discord.com', headers=Header, proxies=dict(http=f"http://{auau}", https=f"http://{auau}"))
        if req.status_code == 200:
            aaa = gratient.purple("Alive Proxy")
            print(f"{Fore.LIGHTBLUE_EX}{aaa} ->{Fore.RESET} {auau}")
            f = open('alive.txt', 'a', encoding='UTF-8')
            f.write(f'{auau}\n')
            f.close()
        else:
            aaa = gratient.yellow(f"{auau} is Not Working\nStatus Code -> {req.status_code}")
            print(aaa)

if __name__ == "__main__":
    NThread = input("何threadにする?  -> ")
    while True:
        Run = True
        while Run:
            if active_count() <= int(NThread):
                try:
                    Thread(target=gen).start()
                except:
                    pass
    else:
            if active_count() <= int(NThread):
                try:
                    Thread(target=gen).start()
                except Exception as e:
                    print("error")
