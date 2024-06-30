import boto3

# Configuração
bucket_name = 'tempomedioimportacao'
file_name = 'tempo-medio-de-importacao-por-regiao-fiscal-consolidado-ATT-utf8.csv'
region_name = 'us-east-1'
aws_access_key_id = 'ASIAU6GDZUFZN7UHUHT2'
aws_secret_access_key = 'nzgPN2S9/+0WOr3Z7clNzN4ZnBX5aY04c5YCgx5L'
aws_session_token = 'IQoJb3JpZ2luX2VjEIz//////////wEaCXVzLWVhc3QtMSJIMEYCIQD1bnqYC+Wb9ywF2U7PYXELUzxML+4z6gmY6tYmEYuBGAIhALxETKMcLN4xhfARdPYnWFcdohcAgn8GFnEp6ObGjAHdKqUDCEUQABoMMzM5NzEzMDQwNzU0IgxosJF/bXrC143hey4qggPBCm4h9pdMty8/HZ793JMjoxg2xW9PQ97s8yXGqz3F3qdH0CqYWB5o9cQVr6q3wSFwpCehuBCDfTkkbTeceLO5LuLaH+xDuvkNh1XNBrW7g8UlT+JYRMBC42sIH0Mwlf8x3Oa8+dMQ7Cmk2o6xg1KRLpgdEfbyXhyJjl4qDjwhA/5OYua6tNCnrxJaZ2/Jt7uNNWH8z+PaBH/if8s7Bt2a9Jybm4uCvcK9Sc5Ihj3dwNpSn3Cyy4SE8axboW13+1QUPYPKJ5jfu1w7S7bbuhvarSGyN0uEXpArpqt3mWTR+R/bITwniP5jQEyF2Rc12d/XwgwuSy111Gc4GD7YMyO9+CT8G+FYUMXgE5FyIx7J7wcAHrU1GwhfbTnf7TOfI5BLkY5eTTgNtFM+GZAVXa9OIqpVKPELW4sCviiOlO6W10Ov6vnigXtTGWJyo1Du5+LzYaEHMTG9009sIAjwRiA8XNXvIh3m0EtgMDRpTSN2+BzvTyJkpez+7bGLRJBPHwvBuDDRhYW0BjqlAdCBPWBzNQvW+Fhlp9H+/VaHrLwBjah7+irtfrw3p8z7iKxnH+/X0W+/btsk+y3w33DYJP4FHDnlzdF0VXlv2vCCGtTqdA663fOgCWdzZeVW6q1wQD55VEKQXYG3E2+Mt4OG+lg55SXmbzKgZ1OQCmYI4QBWdm/T5ZABTI9EwXeNItS7jrdUVcjnh88X93irx2FqDWRHWpdw/SibTBUwdEqBkw335Q=='

def execute_s3_select(query, description):
    try:
        # Iniciar sessão AWS
        session = boto3.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_session_token=aws_session_token
        )
        s3_client = session.client('s3', region_name=region_name)

        # Executar a consulta S3 Select
        response = s3_client.select_object_content(
            Bucket=bucket_name,
            Key=file_name,
            Expression=query,
            ExpressionType='SQL',
            InputSerialization={
                'CSV': {
                    'FileHeaderInfo': 'USE',
                    'RecordDelimiter': '\n',
                    'FieldDelimiter': ',',
                    'QuoteCharacter': '"'
                }
            },
            OutputSerialization={'CSV': {}},
        )

        # Processar e imprimir os resultados da consulta
        print(f"\n{description}")
        print("-" * len(description))
        for event in response['Payload']:
            if 'Records' in event:
                records = event['Records']['Payload'].decode('utf-8')
                print(records.strip())

    except Exception as e:
        print(f"Erro ao executar a consulta S3 Select: {e}")


# Consultas e descrições
query_1 = """
    SELECT *
    FROM S3Object
    WHERE "TMBDI" > '50' AND "ANO DESEMB" > '2015'
    LIMIT 5;
"""
description_1 = "Consulta 1: Cláusula com dois operadores lógicos"

query_2 = """
    SELECT SUM(CAST("TMBDI" AS FLOAT)) AS total_TMBDI, 
           AVG(CAST("TMBDI" AS FLOAT)) AS average_TMBDI
    FROM S3Object;
"""
description_2 = "Consulta 2: Funções de agregação"

query_3 = """
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
"""
description_3 = "Consulta 3: Função condicional, de conversão, de data e de string"

# Executar consultas
execute_s3_select(query_1, description_1)
execute_s3_select(query_2, description_2)
execute_s3_select(query_3, description_3)