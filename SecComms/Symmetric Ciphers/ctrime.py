import requests

# i intend to use a and b and
# perform a bitwise xor operation
def xor_bytes(a, b):
    
    
    
    return bytes([x ^ y for x, y in zip(a, b)])

def encrypt(plaintext):
    return requests.get(f'https://aes.cryptohack.org/ctrime/encrypt/{plaintext}/').json()['ciphertext']




# remove the question mark @
# initialize it

flag  = b'crypto{'



while True:
    len_diff = {}
    original_len = len(encrypt(flag.hex()))
    
    
    
    for i in range(32, 128):
        # take a break and return
        
        b = chr(i).encode()
        new_flag = flag + b
       
    
        new_len = len(encrypt(new_flag.hex() + new_flag.hex()))  
        len_diff[b] = original_len - new_len
        
        
    flag += max(len_diff, key=len_diff.get) 
    print(flag)
    
    if flag[-1] == ord('}'): break