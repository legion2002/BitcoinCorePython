import pybtc

# pk = pybtc.create_private_key()
# print("pk = " + pk)
# pk = "RCJ9Q6kH5ywdRhchVKrxPUFiJE7cGMKFEB8n9zd4VgdNVYzHNedz"


# a = pybtc.sign_message_tanishk("hey", pk, hex=True)
# print(a)
# b = pybtc.verify_signature(a, public, "6865790D0A")
# print(b)
# pybtc.test_function()
msg = "hey"
pk = "RCJ9Q6kH5ywdRhchVKrxPUFiJE7cGMKFEB8n9zd4VgdNVYzHNedz"
public = pybtc.private_to_public_key(pk)
print("public = " + public)

a = pybtc.sign_message_tanishk(msg, pk, hex2=True)
pybtc.verify_message_tanishk(msg , a, public)
# RBFyY5CT65nFp6uz7Kjv9uyP9V2pZuXEZwL4KZvB5tdCw249o7Ew
