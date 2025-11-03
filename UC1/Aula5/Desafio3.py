# 3. Tentativa de Login e Senha 
# Simule um sistema de login simples onde o usuário tem um número limitado de tentativas 
# para digitar a senha correta. 
# ●  Defina um nome de usuário e uma senha corretos (ex: admin e 123456). 
# ●  Dê ao usuário 3 tentativas para acertar a combinação. 
# ●  Se a senha estiver correta, imprima uma mensagem de sucesso e use o comando 
# break para sair do loop. 
# ●  Se a senha estiver errada, informe o erro e diminua o número de tentativas 
# restantes. 
# ●  Se as tentativas acabarem, imprima uma mensagem de bloqueio.
usuario_correto = "admin"
senha_correta = "123456"
tentativas = 3

for i in range(tentativas):
    print("\nTentativa", i + 1)
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Login realizado com sucesso!")
        break
    else:
        restante = tentativas - (i + 1)
        print("Usuário ou senha incorretos.")
        if restante > 0:
            print("Tentativas restantes:", restante)
        else:
            print("Número de tentativas excedido. Conta bloqueada.")
