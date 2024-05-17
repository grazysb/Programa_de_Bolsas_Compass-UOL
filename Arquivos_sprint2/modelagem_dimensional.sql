

CREATE TABLE locacao (
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
	CONSTRAINT locacao_pk PRIMARY KEY (idLocacao),
	CONSTRAINT locacao_quilometragem_FK FOREIGN KEY (idLocacao) REFERENCES quilometragem(idLocacao),
	CONSTRAINT locacao_cliente_FK FOREIGN KEY (idCliente) REFERENCES cliente(idCliente),
	CONSTRAINT locacao_carro_FK FOREIGN KEY (idCarro) REFERENCES carro(idCarro),
	CONSTRAINT locacao_vendedor_FK FOREIGN KEY (idVendedor) REFERENCES vendedor(idVendedor)
);



CREATE TABLE combustivel (
	idCombustivel INT NOT NULL,
	tipoCombustivel VARCHAR,
	CONSTRAINT combustivel_pk PRIMARY KEY (idCombustivel)
);



CREATE TABLE vendedor (
	idVendedor INT NOT NULL,
	nomeVendedor VARCHAR,
	sexoVendedor SMALLINT,
	estadoVendedor VARCHAR,
	CONSTRAINT vendedor_pk PRIMARY KEY (idVendedor)
);



CREATE TABLE carro (
	idCarro INT NOT NULL,
	classiCarro VARCHAR,
	marcaCarro VARCHAR,
	modeloCarro VARCHAR,
	anoCarro INT,
	idCombustivel INT,
	CONSTRAINT carro_pk PRIMARY KEY (idCarro),
	CONSTRAINT carro_combustivel_FK FOREIGN KEY (idCombustivel) REFERENCES combustivel(idCombustivel)
);



CREATE TABLE cliente (
	idCliente INT NOT NULL,
	nomeCliente VARCHAR,
	cidadeCliente VARCHAR,
	estadoCliente VARCHAR,
	paisCliente VARCHAR,
	CONSTRAINT cliente_pk PRIMARY KEY (idCliente)
);



CREATE TABLE quilometragem (
	idLocacao INT NOT NULL,
	kmCarro INT,
	CONSTRAINT quilometragem_pk PRIMARY KEY (idLocacao)
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
