import hashlib

# Message in bytes
message = b"Ceci est un cours de cryptographie"

# MD5 print
md5_hash = hashlib.md5(message).hexdigest()

print("Message :", message.decode())  # decode() to display as string
print("MD5 :", md5_hash)
print("Taille de l'empreinte :", hashlib.md5().digest_size, "octets")