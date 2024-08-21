import sys
from awsglue.transforms import ApplyMapping
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import SparkSession
from awsglue.dynamicframe import DynamicFrame

# Inicialização do contexto do Glue
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Ler dados CSV da Trusted Zone
csv_data = glueContext.create_dynamic_frame.from_catalog(
    database="trusted_data_db",
    table_name="csv",
    transformation_ctx="csv_data"
)

# Ler dados JSON da Trusted Zone
json_data = glueContext.create_dynamic_frame.from_catalog(
    database="trusted_data_db",
    table_name="json",
    transformation_ctx="json_data"
)

# Converter DynamicFrames para DataFrames do Spark
csv_df = csv_data.toDF()
json_df = json_data.toDF()

# Limpar dados CSV: Remover linhas onde todos os valores são nulos
csv_df_cleaned = csv_df.dropna(how='all')

# Limpar dados JSON: Remover linhas onde todos os valores são nulos
json_df_cleaned = json_df.dropna(how='all')

# Remover duplicatas: garantir que não há registros duplicados em cada DataFrame
csv_df_cleaned = csv_df_cleaned.dropDuplicates()
json_df_cleaned = json_df_cleaned.dropDuplicates()

# Realizar a união dos DataFrames com base na coluna 'titulo_original'
joined_df = csv_df_cleaned.join(
    json_df_cleaned,
    csv_df_cleaned["titulo_original"] == json_df_cleaned["titulo_original"],
    "inner"
).select(
    csv_df_cleaned["titulo_original"], 
    csv_df_cleaned["ano_lancamento"].alias("ano_lancamento_csv"),
    csv_df_cleaned["tempo_minutos"], 
    csv_df_cleaned["genero"], 
    csv_df_cleaned["nota_media"].alias("nota_media_csv"), 
    csv_df_cleaned["numero_votos"], 
    csv_df_cleaned["genero_artista"], 
    csv_df_cleaned["personagem"], 
    csv_df_cleaned["nome_artista"], 
    csv_df_cleaned["ano_nascimento"], 
    csv_df_cleaned["ano_falecimento"], 
    csv_df_cleaned["profissao"], 
    csv_df_cleaned["titulos_mais_conhecidos"],
    json_df_cleaned["ano_lancamento"].alias("ano_lancamento_json"),
    json_df_cleaned["nota_media"].alias("nota_media_json"),
    json_df_cleaned["popularidade"],
    json_df_cleaned["idioma_original"],
    json_df_cleaned["ids_genero"]
)

# Mostrar uma amostra dos dados unidos
print("Amostra dos dados unidos:")
joined_df.show(5, truncate=False)

# Converter o DataFrame unido de volta para DynamicFrame
joined_dynamic_frame = DynamicFrame.fromDF(joined_df, glueContext, "joined_dynamic_frame")

# Gravar o DataFrame unido no S3 em formato PARQUET
glueContext.write_dynamic_frame.from_options(
    frame=joined_dynamic_frame,
    connection_type="s3",
    connection_options={
        "path": "s3://mybucket-raw-zone/trusted/new_joined_movies/",
        "partitionKeys": []  
    },
    format="parquet",
    transformation_ctx="output_data"
)

job.commit()
