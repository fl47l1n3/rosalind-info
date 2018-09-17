"""
http://rosalind.info/problems/grph/

Given: A collection of DNA strings in FASTA format having total length at
most 10 kbp.

Return: The adjacency list corresponding to O3O3. You may return edges in
any order.
"""

from __future__ import division
from collections import defaultdict
import sys


def adjacency(fasta, k):
    result = []
    for h1, d1 in fasta.iteritems():
        for h2, d2 in fasta.iteritems():
            if h1 != h2 and d1[-k:] == d2[:k]:
                result.append((h1, h2))
    return result


def get_fasta(data):
    fasta = defaultdict(str)
    current_header = None
    for line in data:
        if line.startswith('>'):
            current_header = line.strip().replace('>', '')
        else:
            fasta[current_header] += line.strip()
    return fasta


data = sys.stdin.readlines()
fasta = get_fasta(data)
for p in adjacency(fasta, 3):
    print(' '.join(p))
