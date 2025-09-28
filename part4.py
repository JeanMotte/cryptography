import hashlib

mot_de_passe = b"secret123"
hash_stocke = hashlib.sha256(mot_de_passe).hexdigest()
# Simulation d’une connexion
essai = input("Entrez le mot de passe : ").encode()
if hashlib.sha256(essai).hexdigest() == hash_stocke:
 print("■ Mot de passe correct")
else:
 print("■ Mot de passe incorrect")
