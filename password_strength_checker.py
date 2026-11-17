# PassGuard - Password Strength Checker
import string
import colorama, subprocess, time, sys, os, random


def exit_program():
    choice = input("Press any key to continue or 'q' to exit: ")
    if choice == 'q' or choice == 'Q':
        exit()    
    start()

def create_random_password():
    length_input = input("Set the length of the password: ")
    if not length_input.isdigit():
        print(colorama.Fore.LIGHTRED_EX + "[!] " + colorama.Style.RESET_ALL + "Please enter a digit.")
        create_random_password()
    length = int(length_input)
    length_upper = int(length * 0.25)
    length_lower = int(length * 0.25)
    length_digit = int(length * 0.25)
    length_special = int(length * 0.25) 

    current_length = length_upper + length_lower + length_digit + length_special
    remaining_length = length - current_length
    final_length = round(current_length + remaining_length)

    string_upper = string.ascii_uppercase
    string_lower = string.ascii_lowercase
    string_digit = string.digits
    string_special = string.punctuation

    final_list = []
    final_list.extend(random.choice(string_upper) for i in range(length_upper))
    final_list.extend(random.choice(string_lower) for i in range(length_lower))
    final_list.extend(random.choice(string_digit) for i in range(length_digit))
    final_list.extend(random.choice(string_special) for i in range(length_special))
    random.shuffle(final_list)
    random_pass = ''.join(final_list)
    print(random_pass)
    exit_program()

def check_password():

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

def start():
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

    intro = f'{name.replace("D", colorama.Back.MAGENTA + " " + colorama.Style.RESET_ALL).replace("I", colorama.Back.MAGENTA + " " + colorama.Style.RESET_ALL).replace("H", colorama.Style.DIM + colorama.Back.MAGENTA + " " + colorama.Style.RESET_ALL).replace("S", colorama.Back.MAGENTA + " " + colorama.Style.RESET_ALL).replace("Y", colorama.Back.MAGENTA + " " + colorama.Style.RESET_ALL).replace("d", colorama.Back.WHITE + " " + colorama.Style.RESET_ALL).replace("j", "▀" + colorama.Style.RESET_ALL)}'
    print(intro)
    choice = input("1. Check Password Strength\n2. Generate Random Password\n3. Exit\n" + colorama.Fore.GREEN + "[*] " + colorama.Style.RESET_ALL + "Enter Choice: ")
    if not choice.isdigit():
        print(colorama.Fore.LIGHTRED_EX + "[!] " + colorama.Style.RESET_ALL + "Choose between 1, 2 and 3")
        for i in range(3):
            print("  .", end=" ", flush=True)
            time.sleep(1.5)
        start()
    elif choice == "1":
        check_password()
    elif choice == "2":
        create_random_password()

start()