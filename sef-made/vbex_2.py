#!/usr/bin/python3
from eutils import Client
import csv

# Reading csv file line by line
with open('gene_species.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';', quotechar='|')
    line_count = 0
    for row in csv_reader:
       if line_count == 0:
        print("{0:5s} | {1:5s}".format(row[0],row[1]))
        line_count += 1
       
##################
eclient = Client(api_key="c77ce1e1071a79329dcbc1999a5f6e34a308")
from eutils import Client
gene_efetch = eclient.efetch(db='gene', id=7157)
gene = gene_efetch.entrezgenes[0]

gene_esearch = eclient.esearch(db='protein',term='CDH1 [gene] AND "Homo sapiens"[orgn] AND srcdb refseq [prop]')
print("\nEsearch result:")
print("="*28)

print("Count: {}".format(gene_esearch.count))

# Loop over Ids
print("\nLoop over Ids:")
print("="*14)

for id in gene_esearch.ids:
    protein_efetch = eclient.efetch(db='protein', id=id)
    refseq = protein_efetch.gbseqs[0]
    print(">{}\n{}".format(gene.genus_species,refseq.sequence))




csv_file.close()
