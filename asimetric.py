import rsa

(pubkey, privkey) = rsa.newkeys(512)
message = b"Bezopasnost aiperi"

encrypted = rsa.encrypt(message, pubkey)
decrypted = rsa.decrypt(encrypted, privkey)

print("Открытый ключ: ", pubkey)
print("Закрытый ключ: ", privkey)

print("Зашифрованный сообщение: ", encrypted)
print("Расшифрованный сообщение: ", decrypted)
