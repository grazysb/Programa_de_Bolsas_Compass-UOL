#!/bin/bash

mkdir -p vendas
echo "O diretório vendas foi criado"


cp dados_de_vendas.csv vendas/
mkdir -p vendas/backup
data=$(date +"%Y-%m-%d")
cp dados_de_vendas.csv vendas/backup/dados-$data.csv
mv vendas/backup/dados-$data.csv vendas/backup/backup-dados-$data.csv


data_sistema=$(date +"%Y-%m-%d %H:%M:%S")
arquivo_vendas="dados_de_vendas.csv"
primeira_data=$(awk -F',' 'NR==2 {print $1}' "$arquivo_vendas")
ultima_data=$(tail -n 1 "$arquivo_vendas" | cut -d ',' -f 1)
total_itens=$(awk -F',' 'NR>1 {print $2}' "$arquivo_vendas" | sort -u | wc -l)

echo "Data do sistema: $data_sistema" > relatorio.txt
echo "Data do primeiro registro de venda: $primeira_data" >> relatorio.txt
echo "Data do último registro de venda: $ultima_data" >> relatorio.txt
echo "Quantidade total de itens diferentes vendidos: $total_itens" >> relatorio.txt
echo "As dez primeiras linhas do arquivo $arquivo_vendas são:" >> relatorio.txt
head "$arquivo_vendas" >> relatorio.txt
echo "Relatório gerado com sucesso em relatorio.txt"


zip -r backup-dados-$data.csv.zip vendas/backup/backup-dados-$data.csv


if [ $? -eq 0 ]; then
    echo "Arquivo 'backup-dados-$data.csv' comprimido com sucesso para 'backup-dados-$data.csv.zip'."
else
    echo "Ocorreu um erro ao comprimir o arquivo 'backup-dados'."
fi


arquivo_backup="vendas/backup/backup-dados-$data.csv"
rm "$arquivo_backup"


arquivo_vendas="vendas/dados_de_vendas.csv"
rm "dados_de_vendas.csv"


