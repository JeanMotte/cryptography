# PART 1:
<!-- Results -->
<!-- 
Message : Ceci est un cours de cryptographie
MD5 : 6ac10db26b001261d56251e61ef12a13
 -->
- 16 octets (or 128 bits)
- The entry message does not influence the size of the output hash. 
- The MD5 hash function always produces a fixed-size output of 128 bits (16 bytes), regardless of the input message size.


# PART 2:
<!-- Results -->
<!-- 
SHA-224 : 8a08715e34a37939e33b1570dcd0ab445dc63354f77151cc026e2144
Taille de l'empreinte : 28 octets
 -->
- Difference in size: 16 bytes (MD5) vs 28 bytes (SHA-224)
- A longer hash provides a larger output space, making it exponentially more difficult for attackers to find

# PART 3:
<!-- Results -->
<!-- 
MD5(msg1) : ebc58ab2cb4848d04ec23d83f7ddf985
MD5(msg2) : f02368945726d5fc2a14eb576f7276c0 
-->
- Quand on compare les 2 empreintes, on remarque que les output hash sont différents (mais évidemment de même longueur)
- C'est l'effet d'avalanche dans le sens où la plus petite modification de l'input a pour conséquence un changement significatif et imprévisible de l'output

# PART 4:
<!-- Results -->
<!-- 
Entrez le mot de passe : secret123
■ Mot de passe correct
 -->
 - On stocke l'empreinte du mot de passe (généralement en base de données) ; et pas le mot de passe en clair, dans un souci de sécurité et de confidentialité des données utilisateur. Si le mot de passe est stocké en clair, les persones ayant accès à la base peuvent le lire (e.g. les développeurs). 
 - Une fuite de donnée ou un piratage peut avoir lieu, et donner l'accès à la base aux pirates. Si les pirates ont uniquement accès aux hash, alors il leur est très difficile voire impossible de retrouver le mot de passe original. Cela dépend de la robustesse de l'algorithme utilisé. En revanche, si les mots de passe sont stockés en clair, alors les comptes des utilisateurs sont compromis.