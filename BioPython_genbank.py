#!/usr/bin/env python3
"""
Name:        Sara Nicholson
Date:        4 February 2022
Description: Genbank Retrieval script example
"""

from Bio import Entrez
Entrez.email = "nicholson.s@northeastern.edu"

from Bio import SeqIO

# Fetch genbank entries
with Entrez.efetch(
        db="nucleotide", rettype="gb", retmode="text", id ="515056"
) as handle:
    seq_record1 = SeqIO.read(handle, "gb")
with Entrez.efetch(
        db = "nucleotide", rettype="gb", retmode="text", id = "J01673.1"
) as handle:
    seq_record2 = SeqIO.read(handle, "gb")

# isolate sequences from entries to list
sequences = []
sequences.append(seq_record1.seq)
sequences.append(seq_record2.seq)
print(sequences)

# print features for each genbank sequence
print(seq_record1.features)
print(seq_record2.features)
