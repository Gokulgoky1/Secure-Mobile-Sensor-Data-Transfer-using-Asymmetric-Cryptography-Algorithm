import ecdsa
import Crypto.PublicKey.RSA as RSA
import rsa

# Generate ECC Key
private_key_ecdsa = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
public_key_ecdsa = private_key_ecdsa.get_verifying_key()

# Get size of ECC Key
size_of_private_key_ecdsa = len(private_key_ecdsa.to_string())
size_of_public_key_ecdsa = len(public_key_ecdsa.to_string())

# Generate RSA Key
private_key_rsa = RSA.generate(2048, e=65537)
public_key_rsa = private_key_rsa.publickey()



# Get size of RSA Key
size_of_private_key_rsa = len(private_key_rsa.export_key())
size_of_public_key_rsa = len(public_key_rsa.export_key())

print("ECC Private Key Size: ", size_of_private_key_ecdsa, "bytes")
print("ECC Public Key Size: ", size_of_public_key_ecdsa, "bytes")
print("RSA Private Key Size: ", size_of_private_key_rsa, "bytes")
print("RSA Public Key Size: ", size_of_public_key_rsa, "bytes")


