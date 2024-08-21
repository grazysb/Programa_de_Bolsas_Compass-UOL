CREATE OR REPLACE VIEW trusted_data_db.media_avaliacao_por_idioma AS
SELECT
    idioma_original,
    AVG(nota_media_json) AS media_avaliacao
FROM 
    trusted_data_db.new_fato_filmes
GROUP BY 
    idioma_original
ORDER BY 
    media_avaliacao DESC;


CREATE OR REPLACE VIEW trusted_data_db.piores_avaliacoes AS
SELECT
    titulo_original,
    nota_media_json AS avaliacao,
    popularidade,
    idioma_original,
    ano_lancamento_json
FROM 
    trusted_data_db.new_fato_filmes
WHERE 
    nota_media_json <> 0
ORDER BY 
    avaliacao ASC
LIMIT 10;


CREATE OR REPLACE VIEW trusted_data_db.media_avaliacao_por_decada AS
SELECT
    CONCAT(CAST(FLOOR(EXTRACT(YEAR FROM date_parse(ano_lancamento_json, '%Y-%m-%d'))/10)*10 AS VARCHAR), 's') AS decada,
    AVG(nota_media_json) AS media_avaliacao
FROM 
    trusted_data_db.new_fato_filmes
GROUP BY 
    CONCAT(CAST(FLOOR(EXTRACT(YEAR FROM date_parse(ano_lancamento_json, '%Y-%m-%d'))/10)*10 AS VARCHAR), 's')
ORDER BY 
    media_avaliacao ASC;
