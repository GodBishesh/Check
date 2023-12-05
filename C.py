#Bishesh
import os
import time
from colorama import Fore, Style

text = " Welcome to Bishesh's world "

for i in range(len(text)):
    colored_text = f"{Fore.RED}{text[:i+1]}{Style.RESET_ALL}"
    print(colored_text, end='', flush=True)
    time.sleep(0.2)
    print('\r', end='')
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')
l = '''\033[1;37m
\033[37m
    ╔╗   ╦  ╔═╗  ╦ ╦  ╔═╗  ╔═╗  ╦ ╦ \033[0m\033[31m  
    ╠╩╗  ║  ╚═╗  ╠═╣  ║╣   ╚═╗  ╠═╣\033[0m\033[31m
    ╚═╝  ╩  ╚═╝  ╩ ╩  ╚═╝  ╚═╝  ╩ ╩\033[37m v•1\033[0m\033[31m
'''
print(l)
