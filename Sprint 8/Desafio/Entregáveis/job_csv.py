import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Inicialização do contexto do Glue
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Ler dados CSV da Raw Zone
csv_data = glueContext.create_dynamic_frame.from_catalog(
    database="raw_data",  # Nome do database onde os metadados dos arquivos brutos estão
    table_name="movies_csv",  # Nome da tabela do Glue Data Catalog associada aos arquivos CSV
    transformation_ctx="csv_data"
)

# Aplicar transformações (mapeamento de colunas)
transformed_data = ApplyMapping.apply(
    frame=csv_data,
    mappings=[
        ("id", "string", "id", "string"),
        ("tituloPincipal", "string", "titulo_principal", "string"),
        ("tituloOriginal", "string", "titulo_original", "string"),
        ("anoLancamento", "int", "ano_lancamento", "int"),
        ("tempoMinutos", "int", "tempo_minutos", "int"),
        ("genero", "string", "genero", "string"),
        ("notaMedia", "float", "nota_media", "float"),
        ("numeroVotos", "int", "numero_votos", "int"),
        ("generoArtista", "string", "genero_artista", "string"),
        ("personagem", "string", "personagem", "string"),
        ("nomeArtista", "string", "nome_artista", "string"),
        ("anoNascimento", "int", "ano_nascimento", "int"),
        ("anoFalecimento", "int", "ano_falecimento", "int"),
        ("profissao", "string", "profissao", "string"),
        ("titulosMaisConhecidos", "string", "titulos_mais_conhecidos", "string")
    ],
    transformation_ctx="transformed_data"
)

# Gravar dados no S3 em formato PARQUET
glueContext.write_dynamic_frame.from_options(
    frame=transformed_data,
    connection_type="s3",
    connection_options={
        "path": "s3://trusted-zone-grazy/trusted/csv/movies/",
        "partitionKeys": []  # Nenhuma partição
    },
    format="parquet",
    transformation_ctx="output_data"
)

job.commit()
