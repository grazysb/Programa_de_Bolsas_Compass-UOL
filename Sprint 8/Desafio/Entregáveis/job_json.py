import sys
from awsglue.transforms import *
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

# Ler todos os arquivos JSON da Raw Zone com configuração multiline
json_data_df = spark.read.option("multiline", "true").option("inferSchema", "true").json("s3://mybucket-raw-zone/raw/TMDB/JSON/movies/2024/07/26/")

# Verificar o esquema dos dados JSON
print("Esquema dos dados JSON:")
json_data_df.printSchema()

# Mostrar uma amostra dos dados JSON
print("Amostra dos dados JSON:")
json_data_df.show(5, truncate=False)

# Converter DataFrame do Spark para DynamicFrame
json_data_dynamic = DynamicFrame.fromDF(json_data_df, glueContext, "json_data_dynamic")

# Aplicar transformações (mapeamento de colunas)
transformed_json_data = ApplyMapping.apply(
    frame=json_data_dynamic,
    mappings=[
        ("id", "int", "id", "int"),
        ("title", "string", "title", "string"),
        ("release_date", "string", "release_date", "string"),
        ("vote_average", "float", "vote_average", "float"),
        ("overview", "string", "overview", "string"),
        ("popularity", "float", "popularity", "float"),
        ("original_language", "string", "original_language", "string"),
        ("genre_ids", "string", "genre_ids", "string"),
        ("budget", "string", "budget", "string"),
        ("revenue", "string", "revenue", "string")
    ],
    transformation_ctx="transformed_json_data"
)

# Gravar dados no S3 em formato PARQUET
glueContext.write_dynamic_frame.from_options(
    frame=transformed_json_data,
    connection_type="s3",
    connection_options={
        "path": "s3://trusted-zone-grazy/trusted/json/movies/",
        "partitionKeys": []  # Nenhuma partição
    },
    format="parquet",
    transformation_ctx="output_json_data"
)

job.commit()
