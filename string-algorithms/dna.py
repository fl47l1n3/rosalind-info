"""
http://rosalind.info/problems/dna/

Given: A DNA string ss of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of
times that the symbols 'A', 'C', 'G', and 'T' occur in ss.
"""
import sys
import collections


def count_nucliotides(dna_string, nucliotides):
    freqs = collections.defaultdict(int)
    for symbol in dna_string:
        freqs[symbol] += 1
    return ' '.join(str(freqs[nt]) for nt in nucliotides)


print(
    count_nucliotides(
        dna_string=sys.stdin.readline(),
        nucliotides=['A', 'C', 'G', 'T']
    )
)
