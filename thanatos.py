import bcrypt

senha_plana = request.form.get('password')

bytes_senha = senha_plana.encode('utf-8')
bytes_hash = bcrypt.hashpw(bytes_senha, bcrypt.gensalt())

password_hash = bytes_hash.decode('utf-8')

print("Hash gerado:", bytes_hash.decode('utf-8'))



if bcrypt.checkpw(senha_digitada.encode('utf-8'), bytes_hash):
    print("Sucesso: A senha está correta!")
else:
    print("Erro: Senha incorreta.")
