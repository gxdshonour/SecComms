import requests






from Crypto.Util.Padding import pad, unpad
asscii_letters = [chr(i).encode() for i in range(32, 127)]

def seperate2blocks(data, block_size):
    return [data[i:i+block_size] for i in range(0, len(data), block_size)]

def encrypt(plaintext):
    return requests.get(f'https://aes.cryptohack.org/ecb_oracle/encrypt/{plaintext}/').json()['ciphertext']





try:
    flag = b''
    for iblock in range(4):
        for i in range(16, 0, -1):
            if iblock==0 and i==16: continue
                
                
                
            brute_force_blocks = {seperate2blocks(encrypt("00"*i + (flag + c).hex()),32)[iblock] : c for c in asscii_letters}



            
            x = seperate2blocks(encrypt("00"*i), 32)[iblock]
            flag = flag + brute_force_blocks[x]


            print(flag)


except KeyError: 
    print(flag.decode())