"""
http://rosalind.info/problems/revc/

Given: A DNA string ss of length at most 1000 bp.

Return: The reverse complement scsc of ss.
"""

import sys
import string


def revc(dna_string):
    reversed_dna = ''.join(reversed(dna_string))
    return reversed_dna.translate(string.maketrans('ATCG', 'TAGC'))


print(
    revc(
        dna_string=sys.stdin.readline(),
    )
)
