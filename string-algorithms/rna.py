"""
http://rosalind.info/problems/rna/

Given: A DNA string tt having length at most 1000 nt.

Return: The transcribed RNA string of tt.
"""
import sys


def dna_to_rna(dna_string):
    return dna_string.replace('T', 'U')


print(
    dna_to_rna(dna_string=sys.stdin.readline())
)
