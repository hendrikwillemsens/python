#!/usr/bin/python3
################################################################################
# 6.3 Combine RefSeq and Ensembl data into a refgenes database
################################################################################
# Import required modules
################################################################################
# Create sqlite3 database 
# Connect with UCSC database
################################################################################
# A) Look for genes who have RefSeq transcripts and save in sqlite
################################################################################
# UCSC Table Browser: https://genome.ucsc.edu/cgi-bin/hgTables
# Get RefSeq data from ncbiRefSeq table
# Create table if not exists
# name = NM_nnnnn = refseq_accession_number
# name2 = gene_symbol

# Reading data from UCSC
# Fetch all results
# Iterate over result
    # Save in database
    
# print("\nTotal rows ncbiRefSeq: {}".format(no_rows))
# Check first row of sqlite ncbiRefSeq table

################################################################################
# A) Look for genes who have Ensembl transcripts and save in sqlite
################################################################################
# UCSC Table Browser: https://genome.ucsc.edu/cgi-bin/hgTables
# Get data from kgXref table
# Create table if not exists

# Reading data from UCSC
# Fetch all results
# Iterate over result
    # Save in database
# Check first row of sqlite kgXref table

################################################################################
# B) Search for RefSeq and Ensembl transcripts for each gene
#    and save transcripts (comma-separated)
################################################################################
# Create table with refgenes 
# First loop over ncbiRefSeq genes
    # Save as new gene

# Next loop over kgXref and either update by adding ensembl transcripts to existing gene
# or add new gene record if no refseq exists
# c_gene --> keep using previous counter
# Add if gene does not exist

# Define functions to get RefSeq transcripts
# Define functions to get Ensembl transcripts

# Now we can get the transcripts for each gene
# Get RefSeq transcripts
# Update record with RefSeq transcripts
# Get Ensembl transcripts
# Update record with Ensembl transcripts

################################################################################
# C) Query for genes
# HAVING BOTH REFSEQ AND ENSEMBL TRANSCRIPTS (26040)
# HAVING ONLY REFSEQ TRANSCRIPTS (12683)
# HAVING ONLY ENSEMBL TRANSCRIPTS (32643)
################################################################################
# D) Save results in Excel table
