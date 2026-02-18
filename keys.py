import os # built-in python module that imports the operating system features 
from ecdsa import SigningKey, SECP256k1 # ecdsa is a external crypto library used in Bitcoin and Ethereum / SigningKey is used to sign messages / SECP256k1 is the specific elliptic curve that is used on Bitcoin and Ethereum

class PrivateKey: # All objects coming from this class will know how to generate a private key, derive a public key and sign data
    def __init__(self): # This constructor will run automatically everytime we create a new object like this: pk = PrivateKey()
        self.secret = os.urandom(32) # Here we are generating the private key which means "generating 32 random bytes" / 32 bytes = 256 bits which matches the size required by SECP256k1

        self.signing_key = SigningKey.from_string(
            self.secret,
            curve=SECP256k1
        ) # Here, self.secret is the private key, it turns the private key into something usable - from_string() - and then the object self.signing_key can create a public key and sign data

    def public_key(self): # The public key will be derived from the private key
        vk = self.signing_key.verifying_key
        return b'\x04' + vk.to_string()
    
    def sign(self, data: bytes) -> bytes:
        return self.signing_key.sign(data)
