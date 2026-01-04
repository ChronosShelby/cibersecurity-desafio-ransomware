import pyaes

file_name = "teste.txt"
encrypted_file_name = file_name + ".enc"

try:
    # Abrir o arquivo original
    with open(file_name, "rb") as file:
        file_data = file.read()

    # Chave de criptografia (16 bytes = AES-128)
    key = b"testeransomwares"

    # Criar objeto AES em modo CTR
    aes = pyaes.AESModeOfOperationCTR(key)

    # Criptografar os dados
    crypto_data = aes.encrypt(file_data)

    # Salvar o arquivo criptografado
    with open(encrypted_file_name, "wb") as encrypted_file:
        encrypted_file.write(crypto_data)

    print("Criptografia concluída com sucesso.")
    print(f"Arquivo original preservado: {file_name}")
    print(f"Arquivo criptografado criado: {encrypted_file_name}")

except FileNotFoundError:
    print("Erro: arquivo não encontrado.")

except Exception as erro:
    print(f"Ocorreu um erro inesperado: {erro}")