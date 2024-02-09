#!/usr/bin/env python3
"""
Name:        Sara Nicholson
Date:        4 February 2022
Description: Reads Fasta file using SeqIO and outputs reverse complement
             to sequences in file
"""
import sys
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

# initialize arguments
old_fasta = sys.argv[1]
new_fasta = sys.argv[2]

# Parse original fasta file
headers = []
sequences = []
descriptions = []
for record in SeqIO.parse(old_fasta, "fasta"):
    seq = record.seq
    newseq = seq.reverse_complement()
    descriptions.append(record.description)
    headers.append(record.id)
    sequences.append(str(newseq))


# Zip headers, description and sequences together
new_records = zip(headers, descriptions, sequences)

# Create SeqRecord of zipped elements
records = (SeqRecord(Seq(str(z)), id = str(x), description = str(y)) for x,y,z in new_records)

# Write to new fasta file using SeqIO
SeqIO.write(records, new_fasta, "fasta")

