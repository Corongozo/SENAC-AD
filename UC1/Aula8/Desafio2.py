# 2. Contagem de Caracteres 
# Crie uma função chamada contar_caractere(texto, caractere_procurado): 
# ●  A função deve receber uma string texto e uma string caractere_procurado (de um só 
# caractere). 
# ●  Ela deve retornar o número de vezes que o caractere_procurado aparece no texto. 
# (Não diferencie maiúsculas de minúsculas!) 
# ●  Dica: Use um loop for para percorrer o texto e use .lower() para tratar os caracteres. 
# ●  No programa principal, peça ao usuário uma frase e uma letra, e mostre o resultado 
# da contagem. 
def contar_caractere(texto, caractere_procurado):
    # Converte ambos para minúsculas para não diferenciar maiúsculas de minúsculas
    texto = texto.lower()
    caractere_procurado = caractere_procurado.lower()
    
    contador = 0
    for caractere in texto:
        if caractere == caractere_procurado:
            contador += 1
    return contador

# Programa principal
frase = input("Digite uma frase: ")
letra = input("Digite uma letra para contar: ")

# Verifica se o usuário digitou apenas um caractere
if len(letra) != 1:
    print("Por favor, digite apenas uma letra.")
else:
    resultado = contar_caractere(frase, letra)
    print(f"A letra '{letra}' aparece {resultado} vezes na frase.")
