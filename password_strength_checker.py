#PASSWORD STRENGTH CHECKER
import colorama
import subprocess
import time
import sys
import os

# print(colorama.Back.GREEN + "  " + colorama.Style.RESET_ALL)
os.system('cls' if os.name == 'nt' else 'clear')

name = """
                     DDDDDDDDDDDDD        IIIIIIIIIIIII      HH        HH     HHHHHHHHHHH      SSSSSSSSSSSS       YY      YY      
                    DDD          DD           III           HH        HH     HH        HH     SS                   YY    YY
                   DDD            DD         III           HH        HH     HH        HH     SS                     YY  YY 
                  DDD            DDd        IIId          HHHHHHHHHHHHd    HHHHHHHHHHHd      SSSSSSSSSSSSd           YYYd 
                 DDD            DDd        IIId          HHd       HHd    HHd                          SSd          YYd  
                DDD          DDdd         IIId          HHd       HHd    HHd                          SSd          YYd 
               DDDDDDDDDDDDDDdd      IIIIIIIIIIIIIdd   HHd       HHd    HHd               SSSSSSSSSSSSSd          YYd  
                jjjjjjjjjjjjjj        jjjjjjjjjjjjj    jj        jj     jj                 jjjjjjjjjjjjj          jj
                
    """
def exit_program():
    choice = input("Press any key to continue or 'q' to exit: ")
    if choice == 'q' or choice == 'Q':
        exit()    
    os.system('cls' if os.name == 'nt' else 'clear')
    subprocess.run([sys.executable, 'password_strength_checker.py'])

intro = f'{name.replace("D", colorama.Back.MAGENTA + " " + colorama.Style.RESET_ALL).replace("I", colorama.Back.MAGENTA + " " + colorama.Style.RESET_ALL).replace("H", colorama.Style.DIM + colorama.Back.MAGENTA + " " + colorama.Style.RESET_ALL).replace("S", colorama.Back.MAGENTA + " " + colorama.Style.RESET_ALL).replace("Y", colorama.Back.MAGENTA + " " + colorama.Style.RESET_ALL).replace("d", colorama.Back.WHITE + " " + colorama.Style.RESET_ALL).replace("j", "▀" + colorama.Style.RESET_ALL)}'

print(intro)

password = input(colorama.Fore.YELLOW + "[+]  " + colorama.Style.RESET_ALL + "Enter Your Password to check strength: ")

status = 1

if status == 1:
    if len(password) < 8:
        print(colorama.Fore.LIGHTRED_EX + "[!]  " + colorama.Style.RESET_ALL + "Your password is too short. It should be at least 8 characters long.")
        status = 0

    if not any(char.isupper() for char in password):
        print(colorama.Fore.LIGHTRED_EX + "[!]  " + colorama.Style.RESET_ALL + "Your password should contain at least one uppercase letter.")
        status = 0
        
    if not any(char.islower() for char in password):
        print(colorama.Fore.LIGHTRED_EX + "[!]  " + colorama.Style.RESET_ALL + "Your password should contain at least one lowercase letter.")
        status = 0

    if not any(char.isdigit() for char in password):
        print(colorama.Fore.LIGHTRED_EX + "[!]  " + colorama.Style.RESET_ALL + "Your password should contain at least one digit.")
        status = 0

    if not any(char in "!@#$%^&*()-+" for char in password):
        print(colorama.Fore.LIGHTRED_EX + "[!]  " + colorama.Style.RESET_ALL + "Your password should contain at least one special character.")
        status = 0

if status == 0:
    print("")
else:
    print(colorama.Fore.GREEN + "[$]  " + colorama.Style.RESET_ALL + "Your password is strong enough.")
    time.sleep(2)

exit_program()