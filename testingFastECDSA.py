from fastecdsa import curve, ecdsa, keys


m = "hey"  # some message

""" use default curve and hash function (P256 and SHA2) """
private_key = keys.gen_private_key(curve.secp256k1)
public_key = keys.get_public_key(private_key, curve.secp256k1)
print(private_key)
# private_key = 'Kz36wrYMg9cnKmpV6aucemPa1EAoxwKRo5DBsBML7dLbXbgcsE6K'
public_key = keys.get_public_key(private_key, curve.secp256k1)


pub = PublicKey.fromString()
# standard signature, returns two integers
# r, s = ecdsa.sign(m, private_key, curve = curve.secp256k1)

# should return True as the signature we just generated is valid.
valid = ecdsa.verify((r, s), m, public_key, curve=curve.secp256k1)
