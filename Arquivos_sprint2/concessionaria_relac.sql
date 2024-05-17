-- Criar a tabela cliente
CREATE TABLE cliente (
    idCliente INTEGER PRIMARY KEY,
    nomeCliente VARCHAR,
    cidadeCliente VARCHAR,
    estadoCliente VARCHAR,
    paisCliente VARCHAR,
    idCarrro INT NOT NULL
);

-- Criar a tabela carro
CREATE TABLE carro (
    idCarro INTEGER PRIMARY KEY,
    classiCarro VARCHAR,
    marcaCarro VARCHAR,
    modeloCarro VARCHAR,
    anoCarro INT,
    idCombustivel INT,
    idVendedor INTEGER
);

-- Criar a tabela vendedor
CREATE TABLE vendedor (
    idVendedor INTEGER PRIMARY KEY,
    nomeVendedor VARCHAR,
    sexoVendedor VARCHAR,
    estadoVendedor VARCHAR,
    idLocacao INT
);

-- Criar a tabela locacao
CREATE TABLE locacao (
    idLocacao INTEGER PRIMARY KEY,
    dataLocacao DATETIME,
    horaLocacao DATE,
    qtdDiaria INT,
    vlrDiaria DECIMAL,
    dataEntrega DATE,
    horaEntrega TIME
);

-- Criar a tabela quilometragem
CREATE TABLE quilometragem (
    idLocacao INT PRIMARY KEY,
    kmCarro INT
);

-- Criar a tabela combustivel
CREATE TABLE combustivel (
    idCombustivel INTEGER PRIMARY KEY,
    tipoCombustivel VARCHAR
);


INSERT INTO combustivel (idCombustivel, tipoCombustivel)
SELECT DISTINCT idCombustivel, tipoCombustivel 
FROM tb_locacao;

INSERT INTO quilometragem (idLocacao, kmCarro)
SELECT DISTINCT  idLocacao, kmCarro 
FROM tb_locacao;

INSERT INTO locacao (idLocacao, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega)
SELECT DISTINCT idLocacao, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega 
FROM tb_locacao; 

INSERT INTO carro (idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro)
SELECT DISTINCT idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro
FROM tb_locacao;

INSERT INTO cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao;


INSERT INTO vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor 
FROM tb_locacao;





