import random
import os
import time

os.system("mode con cols=75 lines=30")


def encrypt(mes):
    numbers = '0123456789'
    symbols = '@?/\*$%&!'
    alpha = numbers, 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz', symbols
    rand_alpha = ''.join(random.sample(alpha, len(alpha)))

    key_no = random.randint(3, 8)

    hd_message = []
    encryption_key = [key_no, rand_alpha]

    for letter in mes:
        try:
            if letter in rand_alpha:
                i = 0
                while letter != rand_alpha[i]:
                    i += 1

                letter_pos = i + key_no

                if letter_pos >= len(rand_alpha):
                    letter_pos = letter_pos - len(rand_alpha)
                    new_letter = rand_alpha[letter_pos]
                    hd_message.append(new_letter)

                else:
                    new_letter = rand_alpha[letter_pos]
                    hd_message.append(new_letter)

        except Exception as e:
            print(e)
    # END OF LETTERS ENCRYPTION -----------------------------------------------------------------------------
    print_title()
    print('Your Message Encrypted :')
    print('------------------------\n')

    for i in hd_message:
        print(i, end='')

    print('\n')
    print('\n')
    print('Decryption Key :')
    print('------------------------')
    for i in encryption_key:
        print(i, end='')

    print('\n')
    print('\n')


def decrypt(en_mes, de_key):
    print('decrypt')


def print_title():
    os.system('cls')
    print(' ')
    print(' -------------------------------------------------------------------------')
    print(' |                                                                       |')
    print(" |                      SHAN's ENCRYPT & DECRYPTER                       |")
    print(' |                                                                       |')
    print(' -------------------------------------------------------------------------')
    print('\n')


def user_in():
    print_title()
    print(' Select your option.')
    print(' -------------------\n')
    print('  1) Encrypt')
    print('  2) Decryption\n')

    user_selection = input()

    if user_selection == '1':
        print_title()
        print(' Enter your message.')
        print(' -------------------\n')
        message = input()
        encrypt(message)

    elif user_selection == '2':
        print_title()
        print(' Enter your message.')
        print(' -------------------\n')
        message = input()
        print('\n')
        print(' Enter the decryption key.')
        print(' -------------------\n')
        key = input()
        decrypt(message, key)

    else:
        print_title()
        time.sleep(1.5)
        print('\n')
        print('\n')
        print('                        Something went wrong..\n')
        print('\n')
        print('          Please Enter your selection by enter the number. 1 or 2\n')
        time.sleep(3)
        os.system('python3 main.py')


if __name__ == '__main__':
    user_in()
