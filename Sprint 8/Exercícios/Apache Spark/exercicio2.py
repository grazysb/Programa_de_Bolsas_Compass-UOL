from pyspark.sql import SparkSession
from pyspark.sql.functions import expr, lit, col, rand, when, udf
from pyspark.sql.types import StringType
import random

# 1. Criação da sessão Spark
spark = SparkSession.builder \
    .appName("Exercício Intro") \
    .getOrCreate()

# 2. Caminho para o arquivo de texto
arquivo = "/home/grazy/spark_lab/nomes_aleatorios.txt"  # Atualize o caminho conforme necessário

# 3. Caminho para os arquivos CSV de saída
saida_csv_detalhado = "/home/grazy/spark_lab/saida/nomes_aleatorios_completo.csv"  # Atualize o caminho conforme necessário
saida_csv_resumo_geracao = "/home/grazy/spark_lab/saida/quantidade_por_geracao.csv"  # Atualize o caminho conforme necessário
saida_csv_resumo_pais = "/home/grazy/spark_lab/saida/quantidade_por_pais.csv"  # Atualize o caminho conforme necessário

# 4. Leitura do arquivo de texto
df = spark.read.text(arquivo)

# 5. Adiciona uma nova coluna com valores aleatórios entre 1945 e 2010
df = df.withColumn("ano", expr("floor(rand() * (2010 - 1945 + 1)) + 1945"))

# 6. Lista dos países da América do Sul
paises = [
    "Argentina", "Bolívia", "Brasil", "Chile", "Colômbia", 
    "Equador", "Guiana", "Paraguai", "Peru", "Suriname", 
    "Uruguai", "Venezuela", "Guiana Francesa"
]

# 7. Função UDF para gerar um país aleatório
def gerar_pais_aleatorio():
    return random.choice(paises)

# Registrar a função UDF
udf_gerar_pais = udf(gerar_pais_aleatorio, StringType())

# 8. Adiciona uma coluna de país aleatório ao DataFrame principal
df_resultado = df.withColumn("pais", udf_gerar_pais())

# 9. Adiciona coluna de geração com base no ano
df_resultado = df_resultado.withColumn(
    "geracao",
    when(col("ano").between(1946, 1964), "Baby Boomer") \
    .when(col("ano").between(1965, 1980), "Geração X") \
    .when(col("ano").between(1981, 1996), "Geração Y (Millennials)") \
    .otherwise("Geração Z")
)

# 10. Adiciona coluna de quantidade com valor padrão
df_resultado = df_resultado.withColumn("quantidade", lit(1))

# 11. Exibe o resultado
df_resultado.show(truncate=False)

# 12. Salva o DataFrame detalhado em um arquivo CSV
df_resultado.write.csv(saida_csv_detalhado, header=True)

# 13. Calcula a quantidade por geração
resumo_geracao = df_resultado.groupBy("geracao").count().withColumnRenamed("count", "quantidade")

# 14. Salva o resumo da quantidade por geração em um arquivo CSV
resumo_geracao.write.csv(saida_csv_resumo_geracao, header=True)

# 15. Calcula a quantidade por país
resumo_pais = df_resultado.groupBy("pais").count().withColumnRenamed("count", "quantidade")

# 16. Salva o resumo da quantidade por país em um arquivo CSV
resumo_pais.write.csv(saida_csv_resumo_pais, header=True)

# 17. Finaliza a sessão Spark
spark.stop()
