Piores avaliações:
SELECT DISTINCT

    titulo_original,
    nota_media_json AS avaliacao,
    popularidade,
    idioma_original,
    ano_lancamento_json
FROM 
    trusted_data_db.new_fato_filmes
WHERE 
    nota_media_json <> 0
    AND numero_votos >= 100  -- Filtra filmes com pelo menos 100 votos
ORDER BY 
    avaliacao ASC
LIMIT 10;

Média por idioma:
SELECT DISTINCT
    idioma_original,
    AVG(nota_media_json) AS media_avaliacao
FROM 
    trusted_data_db.new_fato_filmes
WHERE
    numero_votos >= 100  -- Filtra filmes com pelo menos 100 votos
GROUP BY 
    idioma_original
ORDER BY 
    media_avaliacao DESC;


Por década:
SELECT
    CONCAT(CAST(FLOOR(CAST(SUBSTRING(ano_lancamento_json, 1, 4) AS INT) / 10) * 10 AS VARCHAR), 's') AS decada,
    AVG(nota_media_json) AS media_avaliacao
FROM 
    trusted_data_db.new_fato_filmes
WHERE
    numero_votos >= 100000  -- Considera apenas filmes com 100000 ou mais votos
GROUP BY 
    CONCAT(CAST(FLOOR(CAST(SUBSTRING(ano_lancamento_json, 1, 4) AS INT) / 10) * 10 AS VARCHAR), 's')
ORDER BY 
    media_avaliacao ASC;
