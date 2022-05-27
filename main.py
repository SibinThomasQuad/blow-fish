from Crypto.Cipher import Blowfish
cipher            = Blowfish.new("SgVkYp2s5v8y/B?E(H+MbQeThWmZq4t6")
encrypted_data    = cipher.encrypt("0123data data is working")
print(encrypted_data)
print(cipher.decrypt(encrypted_data))
