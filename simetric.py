from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

message = b"Informacionaja bezopasnost"
encrypted = cipher.encrypt(message)
decrypted = cipher.decrypt(encrypted)

print("Ключ: ", key)
print("Зашифрованный текст: ", encrypted)
print("Расшифрованный текст: ", decrypted)