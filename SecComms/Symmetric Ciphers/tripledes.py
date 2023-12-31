import requests


def encrypt(key, plaintext):


    return requests.get(f'https://aes.cryptohack.org/triple_des/encrypt/{key}/{plaintext}/').json()['ciphertext']



def encryptFlag(key):
    return requests.get(f'https://aes.cryptohack.org/triple_des/encrypt_flag/{key}/').json()['ciphertext']


key = '00'*8 + 'ff'*8 + '00'*8 


flagEncrypt = encryptFlag(key)


flagDecrypt = encrypt(key, flagEncrypt)
bytes.fromhex(flagDecrypt)