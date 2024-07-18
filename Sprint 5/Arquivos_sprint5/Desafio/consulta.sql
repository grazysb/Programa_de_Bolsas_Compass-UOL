-- Consulta 1: Cláusula com dois operadores lógicos
SELECT *
FROM S3Object
WHERE "TMBDI" > '50' AND CAST("ANO DESEMB" AS INTEGER) > 2015
LIMIT 5;

-- Consulta 2: Funções de agregação
SELECT 
    SUM(CAST("TMBDI" AS FLOAT)) AS total_TMBDI,
    AVG(CAST("TMBDI" AS FLOAT)) AS average_TMBDI
FROM S3Object;

-- Consulta 3: Função condicional, de conversão, de data e de string
SELECT 
    CASE 
        WHEN CAST("TMBDI" AS FLOAT) > 50 THEN 'ALTO'
        ELSE 'BAIXO'
    END AS categoria_TMBDI,
    SUBSTRING("ANO DESEMB", 1, 4) AS ano,
    CHAR_LENGTH("RF DESPACHO") AS tamanho_RF_despacho,
    CAST("TMBDI" AS FLOAT) AS TMBDI_float
FROM S3Object
LIMIT 10;
