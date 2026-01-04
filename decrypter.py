import pyaes

encrypted_file_name = "teste.txt.enc"
decrypted_file_name = "teste.txt"

try:
    # Abrir o arquivo criptografado
    with open(encrypted_file_name, "rb") as file:
        encrypted_data = file.read()

    # Chave de descriptografia
    key = b"testeransomwares"

    # Criar objeto AES em modo CTR
    aes = pyaes.AESModeOfOperationCTR(key)

    # Descriptografar os dados
    decrypted_data = aes.decrypt(encrypted_data)

    # Criar o arquivo descriptografado
    with open(decrypted_file_name, "wb") as new_file:
        new_file.write(decrypted_data)

    print("Descriptografia concluída com sucesso.")
    print(f"Arquivo restaurado: {decrypted_file_name}")

except FileNotFoundError:
    print("Erro: arquivo criptografado não encontrado.")

except Exception as erro:
    print(f"Ocorreu um erro inesperado: {erro}")
