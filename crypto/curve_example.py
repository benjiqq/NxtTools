from curve25519 import *

passphrase = "test"
secret = sha256(passphrase).digest()
message = "hello"

verification_key, signing_key, secret_clamped = curve25519_eckcdsa_keygen(secret)
print 'pubkey', verification_key.encode('hex')
print 'signing key', signing_key.encode('hex')
signature = kcdsa_sign(message, secret)
print 'signature', signature.encode('hex')
assert kcdsa_verify(signature, message, verification_key)
assert not kcdsa_verify(signature[::-1], signature, verification_key)
