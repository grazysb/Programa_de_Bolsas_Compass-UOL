SELECT
    CONCAT(CAST(FLOOR(CAST(SUBSTRING(ano_lancamento_json, 1, 4) AS INT) / 10) * 10 AS VARCHAR), 's') AS decada,
    AVG(avaliacao) AS media_avaliacao
FROM (
    SELECT DISTINCT 
        titulo_original,  -- Considera títulos únicos
        nota_media_json AS avaliacao,
        ano_lancamento_json
    FROM 
        trusted_data_db.new_fato_filmes
    WHERE
        numero_votos >= 100000  -- Considera apenas filmes com 100000 ou mais votos
) AS filmes_unicos
GROUP BY 
    CONCAT(CAST(FLOOR(CAST(SUBSTRING(ano_lancamento_json, 1, 4) AS INT) / 10) * 10 AS VARCHAR), 's')
ORDER BY 
    media_avaliacao ASC;


SELECT
    CONCAT(CAST(FLOOR(CAST(SUBSTRING(ano_lancamento_json, 1, 4) AS INT) / 10) * 10 AS VARCHAR), 's') AS decada,
    COUNT(*) AS total_filmes
FROM (
    SELECT DISTINCT 
        titulo_original,  -- Considera títulos únicos
        ano_lancamento_json
    FROM 
        trusted_data_db.new_fato_filmes
) AS filmes_unicos
GROUP BY 
    CONCAT(CAST(FLOOR(CAST(SUBSTRING(ano_lancamento_json, 1, 4) AS INT) / 10) * 10 AS VARCHAR), 's')
ORDER BY 
    decada ASC;


SELECT 
    idioma_original AS idioma,
    COUNT(*) AS total_filmes
FROM (
    SELECT DISTINCT 
        titulo_original,  -- Considera títulos únicos
        idioma_original
    FROM 
        trusted_data_db.new_fato_filmes
) AS filmes_unicos
GROUP BY 
    idioma_original
ORDER BY 
    total_filmes DESC;


SELECT 
    COUNT(DISTINCT idioma_original) AS total_idiomas
FROM 
    trusted_data_db.new_fato_filmes;
