# Caesar Cipher Tool

## Overview
The **Caesar Cipher Tool** is a simple and efficient encryption and decryption tool implemented using the Caesar Cipher algorithm. This program allows you to securely encrypt and decrypt messages using a user-defined shift (key). It supports a wide range of characters, including uppercase and lowercase letters, digits, special characters, and spaces. Additionally, the tool includes a **tab completion** feature, allowing users to easily autocomplete commands such as `encrypt`, `decrypt`, and `exit` by pressing the **Tab** key.

## Features
- **Encryption**: Encrypts text using the Caesar Cipher algorithm by shifting characters by a user-defined key.
- **Decryption**: Decrypts text encrypted using the Caesar Cipher algorithm, recovering the original message using the same key.
- **Supports Various Characters**: The tool works with uppercase and lowercase letters, numbers, special characters, and spaces.
- **Customizable Key**: Users can choose the shift value (key) for encryption and decryption, which can be any integer within the range of 1 to 94.
- **Tab Completion**: Users can press the **Tab** key to automatically complete commands like `encrypt`, `decrypt`, and `exit`, making the user interface more convenient.

## Supported Characters
The Caesar Cipher tool supports the following characters:
- Lowercase letters: `abcdefghijklmnopqrstuvwxyz`
- Uppercase letters: `ABCDEFGHIJKLMNOPQRSTUVWXYZ`
- Numbers: `0123456789`
- Special characters: `!@#$%^&*()-_=+[]{}|;:'",.<>?/`~ `
- Space: ` ` (space character)

## Installation
1. **Clone the repository** to your local machine:
    ```bash
    git clone https://github.com/RoNiXxCybSeC0101/PRODIGY_CS_TASK1.git
    ```

2. **Install dependencies** (if needed):
    The tool uses the `colorama` library for colored output. You can install it with pip:
    ```bash
    pip install colorama
    ```

## Usage
1. **Run the Program**:
    To start the program, run the Python script in your terminal:
    ```bash
    python3 caesar_cipher.py
    ```

2. **Select Operation**:
    You will be prompted to choose an operation:
    - `encrypt` to encrypt a message.
    - `decrypt` to decrypt a message.
    - `exit` to quit the program.

   **Tab Completion**: When typing the operation (`encrypt`, `decrypt`, or `exit`), you can press the **Tab** key to automatically complete the command. For example:
   - Typing `en` and pressing Tab will complete it to `encrypt`.
   - Typing `de` and pressing Tab will complete it to `decrypt`.

3. **Enter Key**:
    After selecting the operation, you will need to enter the key (a number between 1 and 94) for the cipher. This key will be used to shift characters during encryption and decryption.

4. **Enter Text**:
    Provide the text that you want to encrypt or decrypt. The tool will display the result in the terminal.

## Example

### Encryption:

```
        ******************************************
        ***          CAESAR CIPHER TOOL          ***
        ******************************************
        
Type 'encrypt' to encrypt a message.
Type 'decrypt' to decrypt a message.
Type 'exit' to quit the program.

What would you like to do? (encrypt/decrypt/exit): encrypt

ENCRYPTION MODE SELECTED
Enter the key (1 to 94): 50
Enter the text to encrypt: "Hello World:"

CIPHERTEXT: O'299#Xe#^91MO
```

### Decryption:

```

        ******************************************
        ***          CAESAR CIPHER TOOL          ***
        ******************************************
        
Type 'encrypt' to encrypt a message.
Type 'decrypt' to decrypt a message.
Type 'exit' to quit the program.

What would you like to do? (encrypt/decrypt/exit): decrypt

DECRYPTION MODE SELECTED
Enter the key (1 to 94): 50
Enter the text to decrypt: O'299#Xe#^91MO

PLAINTEXT: "Hello World:"
```
