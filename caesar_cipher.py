#!/bin/python3
import os
from colorama import Fore, Style, init
import re
import readline

# Initialize colorama
init(autoreset=True)

# Constants
CHARACTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:\'",.<>?/`~ '
NUM_CHARACTERS = len(CHARACTERS)

# Function to handle tab completion
def complete(text, state):
    options = ['encrypt', 'decrypt', 'exit']
    matches = [option for option in options if option.startswith(text)]
    if state < len(matches):
        return matches[state]
    else:
        return None

# Set the completer function for tab completion
readline.set_completer(complete)
readline.parse_and_bind("tab: complete")  # Bind the Tab key for completion

# Function: Encryption
def encrypt(plaintext, key):
    ciphertext = ''
    for char in plaintext:
        if char in CHARACTERS:
            index = CHARACTERS.find(char)
            new_index = (index + key) % NUM_CHARACTERS
            ciphertext += CHARACTERS[new_index]
        else:
            ciphertext += char  # Leave unknown characters unchanged
    return ciphertext

# Function: Decryption
def decrypt(ciphertext, key):
    plaintext = ''
    for char in ciphertext:
        if char in CHARACTERS:
            index = CHARACTERS.find(char)
            new_index = (index - key) % NUM_CHARACTERS
            plaintext += CHARACTERS[new_index]
        else:
            plaintext += char  # Leave unknown characters unchanged
    return plaintext

# Function: Main Program
def main():
    while True:
        os.system('clear')  # Clear the terminal for a clean display
        print(f"""
        {Fore.CYAN + Style.BRIGHT}******************************************
        ***          {Fore.YELLOW}CAESAR CIPHER TOOL{Fore.CYAN}          ***
        ******************************************
        """)
        print(f"{Fore.GREEN}Type 'encrypt' to encrypt a message.")
        print(f"{Fore.GREEN}Type 'decrypt' to decrypt a message.")
        print(f"{Fore.GREEN}Type 'exit' to quit the program.{Style.RESET_ALL}")
        print()

        # Using readline for input with tab completion and arrow key navigation
        choice = input(f"{Fore.BLUE}What would you like to do? (encrypt/decrypt/exit): {Style.RESET_ALL}").strip().lower()

        if choice == 'encrypt':
            print(f"\n{Fore.MAGENTA}ENCRYPTION MODE SELECTED{Style.RESET_ALL}")
            key = get_key()
            text = input(f"{Fore.BLUE}Enter the text to encrypt: {Style.RESET_ALL}")
            result = encrypt(text, key)
            print(f"\n{Fore.GREEN}CIPHERTEXT: {Fore.YELLOW}{result}{Style.RESET_ALL}")
        elif choice == 'decrypt':
            print(f"\n{Fore.MAGENTA}DECRYPTION MODE SELECTED{Style.RESET_ALL}")
            key = get_key()
            text = input(f"{Fore.BLUE}Enter the text to decrypt: {Style.RESET_ALL}")
            result = decrypt(text, key)
            print(f"\n{Fore.GREEN}PLAINTEXT: {Fore.YELLOW}{result}{Style.RESET_ALL}")
        elif choice == 'exit':
            print(f"\n{Fore.RED}Thank you for using the Caesar Cipher Tool. Goodbye!{Style.RESET_ALL}")
            break
        else:
            print(f"\n{Fore.RED}Invalid choice. Please type 'encrypt', 'decrypt', or 'exit'.{Style.RESET_ALL}")
        
        input(f"\n{Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")  # Wait before clearing the screen

# Function: Get Key
def get_key():
    while True:
        try:
            key = int(input(f"{Fore.BLUE}Enter the key (1 to 94): {Style.RESET_ALL}").strip())
            if 1 <= key < NUM_CHARACTERS:
                return key
            else:
                print(f"{Fore.RED}Error: Key must be between 1 and {NUM_CHARACTERS - 1}.{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}Error: Please enter a valid integer.{Style.RESET_ALL}")

# Entry Point
if __name__ == "__main__":
    main()

