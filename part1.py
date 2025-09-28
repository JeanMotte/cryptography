import hashlib

# Message in bytes
message = b"Ceci est un cours de cryptographie"

# MD5 print
md5_hash = hashlib.md5(message).hexdigest()

print("Message :", message.decode())  # decode() to display as string
print("MD5 :", md5_hash)
print("Taille de l'empreinte :", hashlib.md5().digest_size, "octets")

# Question 1
print("Taille de l'empreinte en bits :", hashlib.md5().digest_size * 8, "bits") # 16 octets (or 128 bits)

# Question 2
# The entry message does not influence the size of the output hash. 
# The MD5 hash function always produces a fixed-size output of 128 bits (16 bytes), regardless of the input message size.