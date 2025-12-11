from utility import *

CONN = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": ""
}

# Lista de comandos SQL
comandos = [
    "CREATE DATABASE IF NOT EXISTS covid_leitos",
    "USE covid_leitos",
    """
    CREATE TABLE IF NOT EXISTS hospital (
        cnes VARCHAR(20) PRIMARY KEY,
        estado VARCHAR(50),
        municipio VARCHAR(50)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS ocupacao (
        id INT AUTO_INCREMENT PRIMARY KEY,
        dataNotificacao DATETIME,
        cnes VARCHAR(20),
        ocupacaoSuspeitoCli FLOAT,
        ocupacaoSuspeitoUti FLOAT,
        ocupacaoConfirmadoCli FLOAT,
        ocupacaoConfirmadoUti FLOAT,
        ocupacaoCovidCli FLOAT,
        ocupacaoCovidUti FLOAT,
        ocupacaoHospitalarCli FLOAT,
        ocupacaoHospitalarUti FLOAT,
        saidaSuspeitaObitos FLOAT,
        saidaSuspeitaAltas FLOAT,
        saidaConfirmadaObitos FLOAT,
        saidaConfirmadaAltas FLOAT,
        FOREIGN KEY (cnes) REFERENCES hospital(cnes)
    )
    """
]

# Executar
executar_comandos(comandos, CONN)
