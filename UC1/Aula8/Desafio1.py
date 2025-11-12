# 1. Verificador de Ano Bissexto
# Crie uma função chamada eh_bissexto(ano):
# ● A função deve receber um ano (inteiro) como parâmetro.
# ● Ela deve retornar True (Booleano) se o ano for bissexto, e False caso contrário.
# ● Regras do ano bissexto: É divisível por 4, exceto para anos divisíveis por 100, a
# menos que sejam também divisíveis por 400. (Ex: 2000 e 2400 são bissextos; 1900
# e 2100 não são).
# ● No programa principal, peça um ano ao usuário e imprima "O ano X É bissexto" ou
# "O ano X NÃO é bissexto", baseado no retorno da função.

def eh_bissexto(ano):
    try:    
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            return True
        else:
            return False
    except ValueError:
        print("Valor invalido.")


ano = int(input("Digite um ano: "))

if eh_bissexto(ano):
    print(f"O ano {ano} É bissexto.")
else:
    print(f"O ano {ano} NÃO é bissexto.")
