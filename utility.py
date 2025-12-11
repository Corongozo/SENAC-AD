import mysql.connector

def executar_comandos(commamds, conn_info):
    """
    Executa uma lista de comandos SQL usando uma conexão já aberta.
    
    Parâmetros:
    - comandos: lista de strings com comandos SQL
    - conn_info: dicionário com as chaves host, user, password, database
    
    Exemplo:
    executar_comandos([
        "CREATE DATABASE IF NOT EXISTS covid_leitos",
        "USE covid_leitos",
        "CREATE TABLE IF NOT EXISTS hospital (cnes VARCHAR(20) PRIMARY KEY, estado VARCHAR(50), municipio VARCHAR(50))"
    ], CONN)
    """
    conn = mysql.connector.connect(
    host=conn_info["host"],
    user=conn_info["user"],
    password=conn_info["password"],
    database=conn_info["database"]
    )
    cursor = conn.cursor()
    for cmd in commamds:
        cursor.execute(cmd)
    conn.commit()
    cursor.close()
    conn.close()

