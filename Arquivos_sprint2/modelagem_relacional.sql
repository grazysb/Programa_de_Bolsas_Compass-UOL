CREATE TABLE cliente (
	idCliente INT NOT NULL,
	nomeCliente VARCHAR,
	cidadeCliente VARCHAR,
	estadoCliente VARCHAR,
	paisCliente VARCHAR,
	idCarrro INT NOT NULL,
	CONSTRAINT cliente_pk PRIMARY KEY (idCliente)
);

CREATE TABLE carro (
	idCarro INT NOT NULL,
	classiCarro VARCHAR,
	marcaCarro VARCHAR,
	modeloCarro VARCHAR,
	anoCarro INT,
	idCombustivel INT,
	idVendedor INTEGER,
	CONSTRAINT carro_pk PRIMARY KEY (idCarro)
);

CREATE TABLE vendedor (
	idVendedor INT,
	nomeVendedor VARCHAR,
	sexoVendedor VARCHAR,
	estadoVendedor VARCHAR,
	idLocacao INT,
	CONSTRAINT vendedor_pk PRIMARY KEY (idVendedor)
);


CREATE TABLE locacao (
	idLocacao INT,
	dataLocacao DATETIME,
	horaLocacao DATE,
	qtdDiaria INT,
	vlrDiaria DECIMAL,
	dataEntrega DATE,
	horaEntrega TIME,
	CONSTRAINT locacao_pk PRIMARY KEY (idLocacao)
);


CREATE TABLE quilometragem (
	idLocacao INT,
	kmCarro INT,
	CONSTRAINT quilometragem_pk PRIMARY KEY (idLocacao)
);


CREATE TABLE combustivel (
	idCombustivel INT NOT NULL,
	tipoCombustivel VARCHAR,
	CONSTRAINT combustivel_pk PRIMARY KEY (idCombustivel)
);




CREATE TEMPORARY TABLE temp AS
SELECT
  idCliente,
  nomeCliente,
  cidadeCliente,
  estadoCliente,
  paisCliente,
  idCarro
FROM cliente;

DROP TABLE cliente;

CREATE TABLE cliente (
	idCliente INT NOT NULL,
	nomeCliente VARCHAR,
	cidadeCliente VARCHAR,
	estadoCliente VARCHAR,
	paisCliente VARCHAR,
	idCarro INT,
	CONSTRAINT cliente_pk PRIMARY KEY (idCliente),
	CONSTRAINT cliente_carro_FK FOREIGN KEY (idCarro) REFERENCES carro(idCarro)
);
CREATE UNIQUE INDEX sqlite_autoindex_cliente_1 ON cliente (idCliente);

INSERT INTO cliente
 (idCliente,
  nomeCliente,
  cidadeCliente,
  estadoCliente,
  paisCliente,
  idCarro)
SELECT
  idCliente,
  nomeCliente,
  cidadeCliente,
  estadoCliente,
  paisCliente,
  idCarro
FROM temp;

DROP TABLE temp;




CREATE TEMPORARY TABLE temp AS
SELECT
  idCarro,
  classiCarro,
  marcaCarro,
  modeloCarro,
  anoCarro,
  idCombustivel,
  idVendedor
FROM carro;

DROP TABLE carro;

CREATE TABLE carro (
	idCarro INT NOT NULL,
	classiCarro VARCHAR,
	marcaCarro VARCHAR,
	modeloCarro VARCHAR,
	anoCarro INT,
	idCombustivel INT,
	idVendedor INTEGER,
	CONSTRAINT carro_pk PRIMARY KEY (idCarro),
	CONSTRAINT carro_vendedor_FK FOREIGN KEY (idVendedor) REFERENCES vendedor(idVendedor),
	CONSTRAINT carro_combustivel_FK FOREIGN KEY (idCombustivel) REFERENCES combustivel(idCombustivel)
);
CREATE UNIQUE INDEX sqlite_autoindex_carro_1 ON carro (idCarro);

INSERT INTO carro
 (idCarro,
  classiCarro,
  marcaCarro,
  modeloCarro,
  anoCarro,
  idCombustivel,
  idVendedor)
SELECT
  idCarro,
  classiCarro,
  marcaCarro,
  modeloCarro,
  anoCarro,
  idCombustivel,
  idVendedor
FROM temp;

DROP TABLE temp;



CREATE TEMPORARY TABLE temp AS
SELECT
  idCarro,
  classiCarro,
  marcaCarro,
  modeloCarro,
  anoCarro,
  idCombustivel,
  idVendedor
FROM carro;

DROP TABLE carro;

CREATE TABLE carro (
	idCarro INT NOT NULL,
	classiCarro VARCHAR,
	marcaCarro VARCHAR,
	modeloCarro VARCHAR,
	anoCarro INT,
	idCombustivel INT,
	idVendedor INTEGER,
	CONSTRAINT carro_pk PRIMARY KEY (idCarro),
	CONSTRAINT carro_vendedor_FK FOREIGN KEY (idVendedor) REFERENCES vendedor(idVendedor),
	CONSTRAINT carro_combustivel_FK FOREIGN KEY (idCombustivel) REFERENCES combustivel(idCombustivel)
);
CREATE UNIQUE INDEX sqlite_autoindex_carro_1 ON carro (idCarro);

INSERT INTO carro
 (idCarro,
  classiCarro,
  marcaCarro,
  modeloCarro,
  anoCarro,
  idCombustivel,
  idVendedor)
SELECT
  idCarro,
  classiCarro,
  marcaCarro,
  modeloCarro,
  anoCarro,
  idCombustivel,
  idVendedor
FROM temp;

DROP TABLE temp;




CREATE TEMPORARY TABLE temp AS
SELECT
  idVendedor,
  nomeVendedor,
  sexoVendedor,
  estadoVendedor,
  idLocacao
FROM vendedor;

DROP TABLE vendedor;

CREATE TABLE vendedor (
	idVendedor INT,
	nomeVendedor VARCHAR,
	sexoVendedor VARCHAR,
	estadoVendedor VARCHAR,
	idLocacao INT,
	CONSTRAINT vendedor_pk PRIMARY KEY (idVendedor),
	CONSTRAINT vendedor_locacao_FK FOREIGN KEY (idLocacao) REFERENCES locacao(idLocacao)
);
CREATE UNIQUE INDEX sqlite_autoindex_vendedor_1 ON vendedor (idVendedor);

INSERT INTO vendedor
 (idVendedor,
  nomeVendedor,
  sexoVendedor,
  estadoVendedor,
  idLocacao)
SELECT
  idVendedor,
  nomeVendedor,
  sexoVendedor,
  estadoVendedor,
  idLocacao
FROM temp;

DROP TABLE temp;




CREATE TEMPORARY TABLE temp AS
SELECT
  idLocacao,
  dataLocacao,
  horaLocacao,
  qtdDiaria,
  vlrDiaria,
  dataEntrega,
  horaEntrega
FROM locacao;

DROP TABLE locacao;

CREATE TABLE locacao (
	idLocacao INT,
	dataLocacao DATETIME,
	horaLocacao DATE,
	qtdDiaria INT,
	vlrDiaria DECIMAL,
	dataEntrega DATE,
	horaEntrega TIME,
	CONSTRAINT locacao_pk PRIMARY KEY (idLocacao),
	CONSTRAINT locacao_quilometragem_FK FOREIGN KEY (idLocacao) REFERENCES quilometragem(idLocacao)
);
CREATE UNIQUE INDEX sqlite_autoindex_locacao_1 ON locacao (idLocacao);

INSERT INTO locacao
 (idLocacao,
  dataLocacao,
  horaLocacao,
  qtdDiaria,
  vlrDiaria,
  dataEntrega,
  horaEntrega)
SELECT
  idLocacao,
  dataLocacao,
  horaLocacao,
  qtdDiaria,
  vlrDiaria,
  dataEntrega,
  horaEntrega
FROM temp;

DROP TABLE temp;




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



