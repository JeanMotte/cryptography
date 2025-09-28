import hashlib

msg1 = b"Bonjour"
msg2 = b"bonjour" # seule la majuscule change
print("MD5(msg1) :", hashlib.md5(msg1).hexdigest())
print("MD5(msg2) :", hashlib.md5(msg2).hexdigest())