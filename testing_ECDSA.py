import ecdsa

 
sk = ecdsa.SigningKey.from_string(bytes.fromhex('4B7A33367772594D6739636E4B6D705636617563656D50613145416F78774B526F35444273424D4C37644C62586267637345364B'), curve=ecdsa.SECP256k1)
signature = sk.sign(b'hey')
print(signature) 