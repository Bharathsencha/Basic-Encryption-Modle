import random
import os

def rotate_right(cp, shift, bits=21):
    return ((cp >> shift) | (cp << (bits - shift))) & ((1 << bits) - 1)

def decrypt_password(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        seed_hex = f.readline().strip()
        encrypted_str = f.read()

    seed = bytes.fromhex(seed_hex)
    seed_int = int.from_bytes(seed, 'big')
    rng = random.Random(seed_int)

    encrypted_list = list(encrypted_str)

    for i in range(min(5, len(encrypted_list))):
        cp = ord(encrypted_list[i])
        rotated = rotate_right(cp, 3) % 0x110000  # Ensure valid range
        encrypted_list[i] = chr(rotated)

    encrypted_str = ''.join(encrypted_list)

    decrypted_chars = []
    i = 0
    while i < len(encrypted_str):
        masks = [rng.randint(0, 0x10FFFF) for _ in range(5)]
        enc_chunk = encrypted_str[i:i+5]
        decrypted = None
        for cp in map(ord, enc_chunk):
            for mask in masks:
                candidate = cp ^ mask
                if 32 <= candidate <= 126:  # printable ASCII range
                    decrypted = chr(candidate)
                    break
            if decrypted:
                decrypted_chars.append(decrypted)
                break
        i += 5

    return ''.join(decrypted_chars)

if __name__ == "__main__":
    file_path = os.path.join(os.getcwd(), "encrypted.txt")
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
    else:
        password = decrypt_password(file_path)
        print(f" Decrypted password: {password}")
