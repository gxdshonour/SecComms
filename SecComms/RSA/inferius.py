from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD

e = 3
n = 742449129124467073921545687640895127535705902454369756401331
ct = 39207274348578481322317340648475596807303160111338236677373  # cipher txt

#with factor.db
p = 752708788837165590355094155871
q = 986369682585281993933185289261

phi = (p-1)*(q-1)

d = inverse(e,phi)

a = pow(ct,d,n)
m = long_to_bytes(a)
print(m)
