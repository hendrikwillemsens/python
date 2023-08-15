#!/usr/bin/python3
################################################################################
# 7.3
# URL: https:/.../protein/?term=DSG*+%5Bgene%5D+AND+%22Mus+musculus%22+%5Borganism%5D%E2%80%8B
# esearch term='DSG* [gene] AND "Mus+musculus" [orgn] AND srcdb refseq [prop]')
################################################################################
from eutils import Client
eclient = Client(api_key="ea092cc6c2c46b29dbad7c00b5946d7b4408")
print("\nUsing NCBI E-utilities in Python\n")

# ESEARCH
# https://www.ncbi.nlm.nih.gov/protein/?term=DSG*+%5Bgene%5D+AND+%22mus+musculus%22%5Borgn%5D
gene_esearch = eclient.esearch(db='protein',term='DSG* [gene] AND "Mus musculus" [orgn] AND srcdb refseq [prop]')
print("\nEsearch result:")
print("="*28)
print("Count: {}".format(gene_esearch.count))
print("Retmax: {}".format(gene_esearch.retmax))
print("Retstart: {}".format(gene_esearch.retstart))
print("Ids: {}".format(gene_esearch.ids))

# EFETCH
# Try efetch for first Id
print("\n1st gene Id: {}".format(gene_esearch.ids[0]))
protein_efetch = eclient.efetch(db='protein', id=gene_esearch.ids[0])
# What can we use?
obj_summary_list = dir(protein_efetch)
print(obj_summary_list)

# gbseqs
refseq = protein_efetch.gbseqs[0]
print("\nRefSeq using gbseq: {}\n{}".format(refseq,type(refseq)))

# What can we use?
refseq = protein_efetch.gbseqs[0]
refseq_list = dir(refseq)
print(refseq_list)

print("acv: {}".format(refseq.acv))
print("cds: {}".format(refseq.cds))
print("gi: {}".format(refseq.gi))
print("locus: {}".format(refseq.locus))
print("organism: {}".format(refseq.organism))

# Loop over Ids
print("\nLoop over Ids:")
print("="*14)
result_file = open("results.fasta","a+")
for id in gene_esearch.ids:
    protein_efetch = eclient.efetch(db='protein', id=id)
    refseq = protein_efetch.gbseqs[0]
    print(">{}\n{}".format(refseq.locus,refseq.sequence))
    result_file.write(">"+refseq.locus+"\n"+refseq.sequence+"\n")
result_file.close()