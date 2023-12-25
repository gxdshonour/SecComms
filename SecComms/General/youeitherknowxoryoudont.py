from pwn import xor

secret = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'

secret_bytes = bytes.fromhex(secret)


result = xor(secret_bytes[:7], b'crypto{').decode()




print(result)


result = xor(secret_bytes, b'myXORkey').decode()
print(result)
