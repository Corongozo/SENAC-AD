CREATE DATABASE vendas_online;
USE vendas_online;

-- Tabela produtos:

CREATE TABLE produtos (
	id_produtos INT PRIMARY KEY,
    nome VARCHAR(255),
    categoria VARCHAR(100),
    preco DECIMAL(10, 2),
	estoque int
);

-- DQL (Data Query Language)
SELECT * FROM produtos;

SELECT nome as nome_produto, preco as preço_produto
FROM produtos
WHERE preco < 1000;

SELECT nome, categoria
FROM produtos
WHERE categoria = 'Escritório';

-- --- RETORNO ERRO CSV AULA 03 (Data Injection via Table Data Import Wizard) ---

SET GLOBAL local_infile = 1; -- marcação de aceite para arquivos locais (passo extra 01 junto ao load data)
'OPT_LOCAL_INFILE=1' -- (passo extra 02 junto ao load data) inserir na sua conexão local (edit da conexão >> Advanced >> Others)

LOAD DATA LOCAL INFILE 'C:/Users/nomenamaquina/caminhodiretorio/vendas_produtos.csv' -- Ajuste o caminho no seu banco local
INTO TABLE vendas_online.produtos
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n' -- Aqui: CR LF
IGNORE 1 ROWS -- Pula o cabeçalho 'id_produto,nome...'
(id_produto, nome, categoria, @preco_var, estoque) -- Mapeia colunas
SET preco = REPLACE(@preco_var, '.', '.'); -- Garante que o decimal seja lido corretamente

-- Aula 4:

CREATE TABLE clientes ( 
    id_cliente INT PRIMARY KEY, 
    nome VARCHAR(255), 
    email VARCHAR(255) 
); 

CREATE TABLE pedidos ( 
    id_pedido INT PRIMARY KEY,
    id_cliente INT,
    data_pedido DATE,
    valor_total DECIMAL(10, 2), 
    id_produto INT,
    quantidade INT 
    -- FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente), 
    -- FOREIGN KEY (id_produto) REFERENCES produtos(id_produto) 
);
-- Alternativo
ALTER TABLE pedidos 
ADD CONSTRAINT fk_pedidos_clientes 
FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente); 

-- Aula 5:

SELECT c.nome, p.data_pedido, t.nome as Produto
FROM clientes c
JOIN pedidos p 
ON c.id_cliente = p.id_cliente
JOIN produtos t
ON t.id_produto = p. id_produto;
