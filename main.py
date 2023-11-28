import os

from crypto import encryption, decryption


def main():
    # Logo
    print("""
8b,dPPYba, ,adPPYYba, 8b       d8  ,adPPYba, 8b,dPPYba,   
88P'   "Y8 ""     `Y8 `8b     d8' a8P_____88 88P'   `"8a  
88         ,adPPPPP88  `8b   d8'  8PP""""""" 88       88  
88         88,    ,88   `8b,d8'   "8b,   ,aa 88       88  
88         `"8bbdP"Y8     "8"      `"Ybbd8"' 88       88  
    """)

    print('Please, for correct script works move your file in "data" directory')

    action = input('Choose the desired action: encrypt: 1, decrypt: 2\n(default=1)\n')
    if action == '':
        action = 1
    try:
        action = int(action)
    except ValueError:
        print("[!] Invalid literal, please enter integer number")

    if action == 1:
        encryption.encryption(file=input("Enter file name(test.txt): \n"), password=input('Please enter your password:\n'))
    elif action == 2:
        decryption.decryption(file=input("Enter file name(test.txt): \n"), password=input('Please enter your password:\n'))


if __name__ == '__main__':
    main()
