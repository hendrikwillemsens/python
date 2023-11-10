#!/usr/bin/python3

from eutils import Client
eclient = Client(api_key="c77ce1e1071a79329dcbc1999a5f6e34a308")


gene_esearch = eclient.esearch(db='protein',term='"replicase" AND "Potato yellowing virus" NOT partial ')
print("\nUsing NCBI E-utilities in Python\n")
print("\n\nResults of gene esearch:\n{}".format(gene_esearch))

print("\nProtein esearch summary result:")
print("="*28)
print("Count: {}".format(gene_esearch.count))
print("Ids: {}".format(gene_esearch.ids))
proteine = gene_esearch.ids


#EFETCH
print("Performing efetch results")
print("="*28)

print("\n1st gene Id: {}".format(gene_esearch.ids[0]))
protein_efetch = eclient.efetch(db='protein', id=gene_esearch.ids[0])
obj_summary_list = dir(protein_efetch)

#gbseqs
refseq = protein_efetch.gbseqs[0]
refseq_list = dir(refseq)
print(refseq_list)

for i in gene_esearch.ids:
    print("Performing efetch for {}".format(i))
    print("ID:: {}".format(i))
    print("locus: {}".format(refseq.locus))
    print("created: {}".format(refseq.created))
    print("Definition: {}".format(refseq.definition))
    print("lenght: {}".format(refseq.length))
    print("sequence: {}".format(refseq.sequence))
    print("\n")


    save_file = open('eutils.fasta','w')
    save_file.write(str(">{}".format(refseq.locus)))
    save_file.write(str("\n"))
    save_file.write(refseq.sequence)
    save_file.close()

#######################


