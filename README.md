# Password Encryption & Decryption Tool

This project provides a simple, secure way to encrypt and decrypt passwords using Python. It uses a combination of random masking and bitwise rotation to obfuscate password characters.

## Features

- Encrypts each character with 5 different random masks.
- Applies bitwise rotation for added complexity.
- Uses a secure, randomly generated seed.
- Decryption works only with the original seed and logic.

## Files

- `encrypt.py`: Script to encrypt a password and save it to `encrypted.txt`.
- `decrypt.py`: Script to read from `encrypted.txt` and decrypt the original password.
- `encrypted.txt`: Output file containing the seed and encrypted string.

## How It Works

### Encryption

1. Generates a 16-byte secure seed using `secrets`.
2. Encrypts each character using 5 XOR masks generated from the seed.
3. Applies a circular bitwise left rotation to the first 5 encrypted characters.
4. Writes the seed (hex) and encrypted data to `encrypted.txt`.

### Decryption

1. Reads the seed and encrypted string from `encrypted.txt`.
2. Recreates the RNG using the seed.
3. Reverses the rotation on the first 5 characters.
4. Decrypts the characters by trying the same 5 masks used during encryption.

## Requirements

- Python 3.x

## How to Use

### Encrypt a Password

```bash
python3 encrypt.py
```

Enter your password when prompted. The encrypted output will be saved to `encrypted.txt`.

### Decrypt a Password

```bash
python3 decrypt.py
```

The script will read from `encrypted.txt` and print the decrypted password.

## Notes

- This script is for educational or personal use only.
- Do not use it for encrypting sensitive passwords in production.
- Always ensure `encrypted.txt` is stored securely.
