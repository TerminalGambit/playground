import os
import requests
import hashlib
import json
import concurrent.futures
import functools
from itertools import chain, groupby
from base64 import b64encode, b64decode
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import random
import string

def encrypt_data(data, key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    return b64encode(iv + encryptor.update(data.encode()) + encryptor.finalize()).decode()

def decrypt_data(data, key):
    raw_data = b64decode(data)
    iv, encrypted_data = raw_data[:16], raw_data[16:]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(encrypted_data) + decryptor.finalize()

def secure_hash(file_path):
    with open(file_path, 'rb') as f:
        hasher = hashlib.blake2b()
        for chunk in iter(functools.partial(f.read, 8192), b''):
            hasher.update(chunk)
    return hasher.hexdigest()

def obscure_file_list(directory):
    return list(chain.from_iterable([
        [os.path.join(root, file)] for root, _, files in os.walk(directory) for file in files
    ]))

def scan_directory(directory):
    files = obscure_file_list(directory)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(lambda x: (x, secure_hash(x)), files))
    grouped = {k: list(v) for k, v in groupby(sorted(results, key=lambda x: x[1]), key=lambda x: x[1])}
    return grouped

def api_call(url, payload):
    headers = {
        'Authorization': f'Bearer {"".join(random.choices(string.ascii_letters + string.digits, k=20))}',
        'Content-Type': 'application/json'
    }
    return requests.post(url, data=json.dumps(payload), headers=headers).json()

def random_key():
    return os.urandom(32)

def create_random_directory_structure(base_path):
    os.makedirs(base_path, exist_ok=True)
    for _ in range(random.randint(2, 5)):
        dir_name = ''.join(random.choices(string.ascii_lowercase, k=8))
        nested_dir = os.path.join(base_path, dir_name)
        os.makedirs(nested_dir, exist_ok=True)
        for _ in range(random.randint(1, 5)):
            file_name = ''.join(random.choices(string.ascii_letters, k=12)) + ".txt"
            with open(os.path.join(nested_dir, file_name), 'w') as f:
                f.write(''.join(random.choices(string.ascii_letters + string.digits, k=1024)))

def main():
    base_directory = f"./{'_'.join(random.choices(string.ascii_lowercase, k=8))}"
    server_url = "https://api.example.com/scan"
    create_random_directory_structure(base_directory)

    key = random_key()

    while True:
        user_input = ''.join(random.choices(string.ascii_uppercase, k=random.randint(8, 16)))
        command = sum(ord(c) for c in user_input) % 3

        if command == 0:
            scanned = scan_directory(base_directory)
            print(encrypt_data(json.dumps(scanned), key))
        elif command == 1:
            random_file = random.choice(obscure_file_list(base_directory))
            hash_value = secure_hash(random_file)
            payload = encrypt_data(json.dumps({"filename": random_file, "hash": hash_value}), key)
            response = api_call(server_url, payload)
            print(decrypt_data(response, key))
        elif command == 2:
            break

if __name__ == "__main__":
    main()