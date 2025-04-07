import secrets
import random
import os

def rotate_left(cp, shift, bits=21):
    return ((cp << shift) | (cp >> (bits - shift))) & ((1 << bits) - 1)

def encrypt_password(password, file_path):
    seed = secrets.token_bytes(16)
    seed_int = int.from_bytes(seed, 'big')
    rng = random.Random(seed_int)

    encrypted_parts = []
    for c in password:
        code_point = ord(c)
        masks = [rng.randint(0, 0x10FFFF) for _ in range(5)]
        encrypted_code_points = [code_point ^ mask for mask in masks]
        encrypted_part = ''.join(chr(cp) for cp in encrypted_code_points)
        encrypted_parts.append(encrypted_part)

    encrypted_str = ''.join(encrypted_parts)
    encrypted_list = list(encrypted_str)

    for i in range(min(5, len(encrypted_list))):
        cp = ord(encrypted_list[i])
        rotated = rotate_left(cp, 3) % 0x110000  # Ensure within valid Unicode range
        encrypted_list[i] = chr(rotated)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(f"{seed.hex()}\n")
        f.write(''.join(encrypted_list))

if __name__ == "__main__":
    password = input("Enter password to encrypt: ")
    file_path = os.path.join(os.getcwd(), "encrypted.txt")
    encrypt_password(password, file_path)
    print(f"Encryption completed. File saved to: {file_path}")
