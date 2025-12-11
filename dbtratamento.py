import pandas as pd
import os

# Lista de colunas que você quer remover
COLUNAS_REMOVER = [
    "_id", "origem", "_p_usuario", "estadoNotificacao", "municipioNotificacao",
     "excluido", "validado", "_created_at", "_updated_at", "Unnamed: 0"
]

def carregar_e_limpar(arquivo):
    df = pd.read_csv(arquivo, low_memory=False)

    # Remover colunas indesejadas
    df = df.drop(columns=["Unnamed: 0"], errors="ignore")

    # Converter datas
    df["dataNotificacao"] = pd.to_datetime(df["dataNotificacao"], errors="coerce")

    # Limpar CNES (remover espaços/tabulações)
    df["cnes"] = df["cnes"].astype(str).str.strip()

    # Preencher valores ausentes em numéricos com 0
    num_cols = df.select_dtypes(include=["float64", "int64"]).columns
    df[num_cols] = df[num_cols].fillna(0)

    return df

arquivos = ["covid_cleaned_all.csv"]

# Verificar se os arquivos existem
for f in arquivos:
    print(f, os.path.exists(f))

# Concatenar
df = pd.concat([carregar_e_limpar(f) for f in arquivos], ignore_index=True)



# Salvar
df.to_csv("covid_cleaned_all_updated.csv", index=False)

print("Arquivo salvo em:", os.getcwd())
