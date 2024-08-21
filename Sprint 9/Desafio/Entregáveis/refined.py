import sys
from awsglue.utils import getResolvedOptions
import boto3
from pyspark.sql import SparkSession

# Parâmetros de entrada
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

# Inicializa a sessão Spark
spark = SparkSession.builder.appName("Transformação Camada Refined").getOrCreate()

# Leitura dos dados da camada Trusted
df_trusted = spark.read.format("parquet").load("s3://mybucket-raw-zone/trusted/new_joined_movies/")

# Transformações para a Tabela de Fatos
df_filmes = df_trusted.select(
    "titulo_original", 
    "ano_lancamento_json", 
    "nota_media_json", 
    "popularidade", 
    "idioma_original", 
    "ids_genero", 
    "tempo_minutos",  
    "numero_votos",   
    "ano_lancamento_csv",  
    "genero"  # Gênero do CSV
)

# Filtro por gênero de Ação e Aventura (ids 28 e 12)
df_filmes_acao_aventura = df_filmes.filter(
    df_filmes["ids_genero"].contains("28") | 
    df_filmes["ids_genero"].contains("12")
)

# Gravação dos dados na camada Refined em formato PARQUET
df_filmes_acao_aventura.write.mode("overwrite").parquet("s3://mybucket-raw-zone/refined/new_fato_filmes/")

# Encerrar a sessão Spark
spark.stop()
