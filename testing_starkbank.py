from ellipticcurve.signature import Signature
from ellipticcurve.ecdsa import Ecdsa
from ellipticcurve.privateKey import PrivateKey


# Generate new Keys
privateKey = PrivateKey()
publicKey = privateKey.publicKey()

message = "hey"
r = 8527058862545077774486369341832040246069169038755695790487046196182049109199
s = 99413458135769248622249498534390963365714354856023193516641503783832194549737
priv = "RCwUFQ897YN29uLp3SHyN8HGmmiT7Ao4XMRR6dbYkFgkwff4xVad"
# signOps = "3045022012da24efcd60d6cfcf7325baeb02050a66e96987a2825465b2aa84ff0d0034cf022100dbca05f7c873d8f00151664679927c29f9c6cc5625432e1b19195a3dfe6e87e9"

privateKey = PrivateKey.fromString(priv)
# Generate Signature
signature = Ecdsa.sign(message, privateKey)
# signature = Signature(r, s)
print(signature._toString())

# To verify if the signature is valid
# print(Ecdsa.verify(message, signature, publicKey))
