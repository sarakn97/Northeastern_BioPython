#!/usr/bin/env python3
"""
Name:        Sara Nicholson
Date:        4 February 2022
Description: Creates SeqRecord using BioPython
"""
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_dna
from Bio import SeqIO

# create seq record object
seq_record = SeqRecord(Seq("aaaatgggggggggggccccgtt", generic_dna), id = "#12345", description = "example 1")

# write SeqRecord to genbank file
SeqIO.write(seq_record, "BioPython_seq.gb", "genbank")

