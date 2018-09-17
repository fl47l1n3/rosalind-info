"""
http://rosalind.info/problems/tree/

Given: A positive integer nn (n≤1000n≤1000) and an adjacency list
corresponding to a graph on nn nodes that contains no cycles.

Return: The minimum number of edges that can be added to the graph to produce
a tree.
"""

import sys


def ed(graph_len, edges):
    """ G is connected and has n − 1 edges (Graph theory). """
    return graph_len - edges - 1


data = sys.stdin.readlines()
print(ed(int(data[:1][0]), len(data[1:])))
