# 2. Cadastro de Candidatos 
# Desenvolva um programa que colete dados de 12 pessoas, usando a decisão para filtrar 
# candidatos menores de 18 anos. 
# ●  O programa deve pedir o Ano de Nascimento do candidato. 
# ●  Se for menor de 18, o programa deve informar que ele não pode participar e pular 
# a coleta dos demais dados (telefone, email etc) para esse candidato. 
# ●  Se for maior de 18, o programa prossegue com o input() para os demais dados. 
from datetime import datetime

ano_atual = datetime.now().year

for i in range(1, 13):
    print("\nCandidato", i)
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    idade = ano_atual - ano_nascimento

    if idade < 18:
        print("Candidato menor de 18 anos. Não pode participar.")
        continue  # pula para o próximo candidato

    # Coleta dos demais dados
    telefone = input("Digite o telefone: ")
    email = input("Digite o e-mail: ")

    print("Dados coletados com sucesso!")

