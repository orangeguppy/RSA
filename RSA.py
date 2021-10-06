from Crypto.Util.number import long_to_bytes, bytes_to_long, getPrime

# Convert the byte human readable string into numbers 
ptx = b'Join me at CHF'
m = bytes_to_long(ptx)

# Generate prime numbers 
p = 1628161
q = 19339153

print("p: ", p)
print("q: ", q)

# Create Bob's public key pair [e, n]
n = p * q
e = 101

print("n: ", n)
print("e: ", e)

# Create Bob's private key pair (e, d)
phi = 31487233720320 #(p - 1) * (q - 1)

d = 3117547893101 # pow(e, -1, phi)

print("phi: ", phi)
print("d: ", d)

# Encrypt the message using the public key
c = pow(m, e, n)
print("[+] Alice's ciphertext to send to Bob:", c)

# Now it's Bob's turn to decrypt the ciphertext using his private key
decrypt = pow(c, d, n)
print("[+] Bob has decrypted the cipher, converting back to human readable bytes...")

# Convert back
text = long_to_bytes(decrypt)

# Make sure Bob received the correct message
assert(text == ptx)
print("[+] Message Bob received:", text.decode())
print("[+] RSA working as intended!")