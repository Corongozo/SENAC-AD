# Cadastro Seletivo de Candidatos 
# Use um for loop para iterar 5 vezes. Dentro do loop, use um if/else para checar se o 
# candidato é menor de 18 anos (rejeição). Crie uma lista principal: candidatos_validos = []. 
# Se o candidato for válido, crie um Dicionário (ex: candidato = {'nome': '...', 'email': '...'}). 
# Adicione este Dicionário à lista: candidatos_validos.append(candidato). 
def cadastro(candidatos):
    ano_atual = 2025
    candidatos_validos = []

    for i in range(candidatos):
        try:
            print('-'*90, "\nCandidato", i+1)
            ano_nascimento = int(input("Digite o ano de nascimento: "))
            idade = ano_atual - ano_nascimento

            if idade < 18:
                print("Candidato menor de 18 anos. Não pode participar.")
                estado = False
                candidato = {'nome': i, 'estado': estado}
                continue

            # Coleta dos demais dados
            telefone = input("Digite o telefone: ")
            email = input("Digite o e-mail: ")
            estado = True
            candidato = {'nome': i, 'email': email, 'telefone': telefone, 'estado': estado}
            candidatos_validos.append(candidato)
            print("Dados coletados com sucesso!")
        except ValueError:
            print("Valor inválido.")
    for i in candidatos_validos:
        print(i)
cadastro(2)