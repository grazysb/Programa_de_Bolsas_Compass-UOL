#!/bin/bash

cat dados_de_vendas1.csv dados_de_vendas2.csv dados_de_vendas3.csv > vendas_combinadas.csv


echo "Relatório de Vendas Combinadas" > relatorio_fina.txt
echo "" >> relatorio_fina.txt


for arquivo in "dados_de_vendas1.csv" "dados_de_vendas2.csv" "dados_de_vendas3.csv"; do
    echo "Informações do arquivo $arquivo:" >> relatorio_fina.txt
    echo "" >> relatorio_fina.txt

    
    echo "As dez primeiras linhas do arquivo $arquivo são:" >> relatorio_fina.txt
    head "$arquivo" >> relatorio_fina.txt
    echo "" >> relatorio_fina.txt
done

echo "Relatório combinado gerado com sucesso em relatorio_fina.txt"

