import pandas as pd
import os

# Lista de colunas que você quer remover
COLUNAS_REMOVER = [
    "_id, origem", "_p_usuario", "estadoNotificacao", "municipioNotificacao",
     "excluido", "validado", "_created_at", "_updated_at"
]

def carregar_e_limpar(arquivo):
    """Carrega um CSV e remove colunas indesejadas."""
    df = pd.read_csv(arquivo, dtype={"cnes": str})
    # Remove apenas colunas que existem no arquivo
    df = df.drop(columns=[c for c in COLUNAS_REMOVER if c in df.columns])
    return df

arquivos = ["2020.csv", "2021.csv", "2022.csv"]

# Verificar se os arquivos existem
for f in arquivos:
    print(f, os.path.exists(f))

# Concatenar
df = pd.concat([carregar_e_limpar(f) for f in arquivos], ignore_index=True)



# Salvar
df.to_csv("covid_cleaned_all.csv", index=False)

print("Arquivo salvo em:", os.getcwd())
