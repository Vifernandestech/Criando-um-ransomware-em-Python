import os
import pyaes

# Nome do arquivo criptografado
file_name = "TESTE.TXT.ransomwaretrollhahaha"  
file = open(file_name, "rb")
file_data = file.read()
file.close()

# Chave para descriptografia (mesma usada na criptografia, com tamanho correto)
key = b"testeransomware1"  # Deve ser a mesma chave usada para criptografia
aes = pyaes.AESModeOfOperationCTR(key)

# Descriptografar o arquivo
decrypt_data = aes.decrypt(file_data)

# Remover o arquivo criptografado
os.remove(file_name)

# Criar o arquivo descriptografado
new_file = "TESTE.TXT"
with open(new_file, "wb") as decrypted_file:
    decrypted_file.write(decrypt_data)

print(f"Arquivo {file_name} foi descriptografado com sucesso como {new_file}!")
