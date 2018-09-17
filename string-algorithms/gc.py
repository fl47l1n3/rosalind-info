"""
http://rosalind.info/problems/gc/

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the
GC-content of that string. Rosalind allows for a default error of 0.001 in
all decimal answers unless otherwise stated; please see the note on absolute
error below.
"""
from __future__ import division
from collections import defaultdict
import sys


def gc_percentage(dna_string):
    gc_cnt = dna_string.count('G') + dna_string.count('C')
    return gc_cnt * 100 / len(dna_string)


def get_fasta(data):
    fasta = defaultdict(str)
    current_header = None
    for line in data:
        if line.startswith('>'):
            current_header = line.strip()
        else:
            fasta[current_header] += line.strip()
    return fasta


data = sys.stdin.readlines()
fasta = get_fasta(data)
result = {}
for header, dna_string in fasta.iteritems():
    result[header] = gc_percentage(dna_string)
max_gc = max(result.iteritems(), key=lambda i: i[1])
print('{0}\n{1}'.format(max_gc[0].replace('>', ''), max_gc[1]))
