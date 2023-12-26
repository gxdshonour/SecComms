from Crypto.Util.number import bytes_to_long, long_to_bytes
import base64
import codecs
import random
import telnetlib
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
from sage.all import *

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

    
    
HOST = "socket.cryptohack.org"
PORT = 13380

def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline().decode()
    st = line[line.find('{'):]
    return json.loads(st)

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)
    
tn = telnetlib.Telnet(HOST, PORT)
    
alice = json_recv()
bob = json_recv()
flag = json_recv()

R = GF(alice["p"])
g = R(alice["g"])
A = R(alice["A"])
B = R(bob["B"])

a = A/g
b = B/g

key = b*A
print(decrypt_flag(key, flag['iv'], flag['encrypted']))