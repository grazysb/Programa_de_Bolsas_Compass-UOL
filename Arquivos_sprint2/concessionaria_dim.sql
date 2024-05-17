CREATE TABLE "fato_locacao" (
	idLocacao INT NOT NULL,
	dataLocacao DATETIME,
	horaLocacao TIME,
	qtdDiaria INT,
	vlrDiaria DECIMAL,
	dataEntrega DATE,
	horaEntrega TIME,
	idCliente INT,
	idCarro INT,
	idVendedor INT,
	CONSTRAINT locacao_pk PRIMARY KEY (idLocacao)
);


CREATE TABLE "dim_combustivel" (
	idCombustivel INT NOT NULL,
	tipoCombustivel VARCHAR,
	CONSTRAINT combustivel_pk PRIMARY KEY (idCombustivel)
);


CREATE TABLE "dim_vendedor" (
	idVendedor INT NOT NULL,
	nomeVendedor VARCHAR,
	sexoVendedor SMALLINT,
	estadoVendedor VARCHAR,
	CONSTRAINT vendedor_pk PRIMARY KEY (idVendedor)
);


CREATE TABLE "dim_carro" (
	idCarro INT NOT NULL,
	classiCarro VARCHAR,
	marcaCarro VARCHAR,
	modeloCarro VARCHAR,
	anoCarro INT,
	idCombustivel INT,
	CONSTRAINT carro_pk PRIMARY KEY (idCarro)
);


CREATE TABLE "dim_cliente" (
	idCliente INT NOT NULL,
	nomeCliente VARCHAR,
	cidadeCliente VARCHAR,
	estadoCliente VARCHAR,
	paisCliente VARCHAR,
	CONSTRAINT cliente_pk PRIMARY KEY (idCliente)
);


CREATE TABLE "dim_quilometragem" (
	idLocacao INT NOT NULL,
	kmCarro INT,
	CONSTRAINT quilometragem_pk PRIMARY KEY (idLocacao)
);

INSERT INTO dim_combustivel (idCombustivel, tipoCombustivel)
SELECT DISTINCT idCombustivel, tipoCombustivel 
FROM tb_locacao;

INSERT INTO dim_quilometragem (idLocacao, kmCarro)
SELECT DISTINCT  idLocacao, kmCarro 
FROM tb_locacao;

INSERT INTO fato_locacao (idLocacao, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega)
SELECT DISTINCT idLocacao, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega 
FROM tb_locacao; 

INSERT INTO dim_carro (idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro)
SELECT DISTINCT idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro
FROM tb_locacao;

INSERT INTO dim_cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao;

INSERT INTO dim_vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor 
FROM tb_locacao;

