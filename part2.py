import hashlib

message = b"Ceci est un cours de cryptographie"

sha224_hash = hashlib.sha224(message).hexdigest()
print("SHA-224 :", sha224_hash)
print("Taille de l'empreinte :", hashlib.sha224().digest_size, "octets")

# Question 1
# Difference in size: 16 bytes (MD5) vs 28 bytes (SHA-224)

# Question 2: why longer hash is more secure?
# A longer hash provides a larger output space, making it exponentially more difficult for attackers to find
