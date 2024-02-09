#!/usr/bin/env python3
"""
Name:           Sara Nicholson
Date:           5 February 2022
Description:    For a given fasta file, returns kmers of specified size of                                each fasta entry and the gc content of each kmer using BioPython
"""
from Bio.Seq import Seq
from Bio import SeqIO
import sys
import re

def sliding_window(k, string):
    """ return list of kmers of lenth 'k' in given string """
    kmers = []
    stop = len(string) - k + 1
    for start in range(0, stop):
        kmers.append(string[start:start + k])

    return kmers


def gc_content(string):
    """ return gc content percentage of given string"""
    string = string.lower()
    count = 0
    for nuc in string:
        if nuc in ['g', 'c']:
            count += 1

    return count/len(string)


if __name__ == "__main__":
    # Initializations
    k_size = int(sys.argv[1])
    fasta = str(sys.argv[2])
    sequence = ''
    headers = 0
    
    for record in SeqIO.parse(fasta, "fasta"):
        print(">" + record.id + record.description)
        seq = str(record.seq)
        kmers = sliding_window(k_size, seq)
        for kmer in kmers:
            kmer_gc = gc_content(kmer)
            print("{}\t{:.2f}".format(kmer, kmer_gc))

