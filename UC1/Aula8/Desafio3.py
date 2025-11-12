# 3. Simulador de Dado 
# Usando o módulo random, crie uma função rolar_dado(lados). 
# ●  A função deve receber o número de lados do dado (ex: 6, 10, 20). 
# ●  Ela deve retornar um número aleatório entre 1 e o número de lados (use 
# random.randint(1, lados)). 
# ●  No programa principal, crie um "simulador de batalha": 
# ○  Peça ao usuário para "Rolar para o Ataque (d20)". Chame a função 
# rolar_dado(20). 
# ○  Peça ao usuário para "Rolar para o Dano (d8)". Chame a função 
# rolar_dado(8). 
# ○  Imprima os resultados de cada rolagem. 
import random

def rolar_dado(lados):
    # Retorna um número aleatório entre 1 e o número de lados
    return random.randint(1, lados)

# Programa principal
input("Pressione Enter para rolar para o Ataque (d20)...")
ataque = rolar_dado(20)
print(f"Resultado do Ataque: {ataque}")

input("Pressione Enter para rolar para o Dano (d8)...")
dano = rolar_dado(8)
print(f"Resultado do Dano: {dano}")
