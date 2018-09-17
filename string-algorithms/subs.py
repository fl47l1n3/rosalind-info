"""
http://rosalind.info/problems/subs/

Given: Two DNA strings ss and tt (each of length at most 1 kbp).

Return: All locations of tt as a substring of ss.
"""


def subs(dna_string, pattern, start, result):
    index = dna_string.find(pattern, start)
    if index != -1:
        result.append(index + 1)
        return subs(dna_string, pattern, index + 1, result)
    else:
        return result


dna_string = 'GATATATGCATATACTT'
positions = ' '.join(map(str, subs(dna_string, 'ATAT', 0, [])))
print(positions)
