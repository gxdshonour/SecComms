# Import 'unhexlify'
from binascii import unhexlify

# Define 'brute' for decryption.

def brute(input, key):
    # Check  lengths of 'input' and 'key' equal / no
    if len(input) != len(key):
        return "Failed!"  

    output = b''  

    
    for b1, b2 in zip(input, key):
        output += bytes([b1 ^ b2])

    try:
        return output.decode("utf-8")  
    except:
        return "Cannot Decode some bytes" 


mystring = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

# Convert mystring to bytes and print it

cipher = unhexlify(mystring)
print("[-] CIPHER: {}".format(cipher))




key_part = brute(cipher[:7], "crypto{".encode())
print("[-] PARTIAL KEY FOUND: {}".format(key_part))



key = (key_part + "y").encode()
key += key * int((len(cipher) - len(key)) / len(key))
key += key[:((len(cipher) - len(key)) % len(key))]
print("[-] Decoding using KEY: {}".format(key))



# Use extended key to decrypt 'cipher' and print result

plain = brute(cipher, key)
print("\n[*] FLAG: {}".format(plain))
