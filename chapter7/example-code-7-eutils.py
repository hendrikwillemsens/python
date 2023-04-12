#!/usr/bin/python3
################################################################################
# E-utilities (example-code-7-eutils.py)
################################################################################
from eutils import Client
# Initialize client that handles all caching and query
# Using API key from NCBI account settings e.g. 
eclient = Client(api_key="84c4d9fa268d5e41511ce024a0cf00537808")
print("\nUsing NCBI E-utilities in Python\n")
################################################################################
# ESEARCH: search for e.g. genes, any valid NCBI query may be used
################################################################################
gene_esearch = eclient.esearch(db='gene',term='tumor necrosis factor')
print("\n\nResults of gene esearch:\n{}".format(gene_esearch))
obj_summary_list = dir(gene_esearch)
print(obj_summary_list)
# Gene esearch summary result
print("\nGene esearch summary result:")
print("="*28)
print("Count: {}".format(gene_esearch.count))
print("Retmax: {}".format(gene_esearch.retmax))
print("Retstart: {}".format(gene_esearch.retstart))
print("Ids: {}".format(gene_esearch.ids))
# First two Ids: [114254422, 7157,...]
print("1st gene Id: {}".format(gene_esearch.ids[0]))
print("2nd gene Id: {}".format(gene_esearch.ids[1]))
################################################################################
# EFETCH: get record using Id e.g. gene id 7157 for human TNF
################################################################################
gene_efetch = eclient.efetch(db='gene', id=7157)
print("\n\nResults of gene efetch:\n{}".format(gene_efetch))
# One may fetch multiple genes at a time
# These are returned as an EntrezgeneSet
# Get first (and only) child which returns instance of Entrezgene class
gene = gene_efetch.entrezgenes[0]
# Gene object attributes
print("\nGene object attributes:")
gene_obj_list = dir(gene)
print(gene_obj_list)
################################################################################
# Easily access some basic information about the gene
print("\nGene information:")
print("="*17)
print("HGNC: {}".format(gene.hgnc))
print("Location: {}".format(gene.maploc))
print("Description: {}".format(gene.description))
print("Gene type: {}".format(gene.type))
print("Species: {}".format(gene.genus_species))
################################################################################
# Get data in for loop
retmax = 5
for retstart in range(retmax):
    gene_id = gene_esearch.ids[retstart]
    gene_efetch = eclient.efetch(db='gene', id=gene_id)
    print("\nGene Id: {}".format(gene_id))
    this_gene = gene_efetch.entrezgenes[0]
    print("HGNC: {}".format(this_gene.hgnc))
    print("Species: {}".format(this_gene.genus_species))
################################################################################