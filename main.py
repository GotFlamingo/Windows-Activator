
import os
from os import system
import time
from colorama import Fore

Home = "TX9XD-98N7V-6WMQ6-BX7FG-H8Q99"
Pro =  "W269N-WFGWX-YVC9B-4J6C9-T83GX"
Edu = "NW6C2-QMPVW-D7KKK-3GKT6-VCFB2"
Ent = "NPPR9-FWDCX-D2C8J-H872K-2YT43"

logo = f'''{Fore.LIGHTMAGENTA_EX}
            .-.
           ((`-)
            \\
             \\
      .="""=._))
     /  .,   .'
    /__(,_.-'
   `    /|
       /_|__
         | `))
         |
{Fore.LIGHTRED_EX}Made BY GoT Flamingo
{Fore.LIGHTYELLOW_EX}Github.com/gotflamingo 
'''
print(logo)
print(f"{Fore.CYAN}Vælg Hvad Du vil have!{Fore.WHITE}")

print(f"{Fore.LIGHTCYAN_EX}[{Fore.WHITE}1{Fore.LIGHTCYAN_EX}]{Fore.WHITE} Windows Key Home")
print(f"{Fore.LIGHTCYAN_EX}[{Fore.WHITE}2{Fore.LIGHTCYAN_EX}]{Fore.WHITE} Windows Key Pro")
print(f"{Fore.LIGHTCYAN_EX}[{Fore.WHITE}3{Fore.LIGHTCYAN_EX}]{Fore.WHITE} Windows Key Educational")
print(f"{Fore.LIGHTCYAN_EX}[{Fore.WHITE}4{Fore.LIGHTCYAN_EX}]{Fore.WHITE} Windows Key Enterprise")
print(" ")
choice = input(f"{Fore.LIGHTWHITE_EX}Hvad Vælger Du? ")


if choice.lower()=="1":
    os.system(f"slmgr /ipk {Home}")        
    
if choice.lower()=="2":
    os.system(f"slmgr /ipk {Pro}")
   
    
if choice.lower()=="3":
    os.system(f"slmgr /ipk {Edu}")
    
    
if choice.lower()=="4":
    os.system(f"slmgr /ipk {Ent}")
    
time.sleep(1)
print(f"{Fore.LIGHTCYAN_EX}[{Fore.WHITE}+{Fore.LIGHTCYAN_EX}]{Fore.WHITE}Tjekker License!")
os.system("slmgr /skms kms8.msguides.com")
print(" ")
time.sleep(1)
print(f"{Fore.LIGHTCYAN_EX}[{Fore.WHITE}+{Fore.LIGHTCYAN_EX}]{Fore.WHITE}Færdig")
os.system("slmgr /ato")
time.sleep(1)
print(" ")
print(f"{Fore.LIGHTMAGENTA_EX}Hav En god Dag")
time.sleep(4)