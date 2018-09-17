"""
http://rosalind.info/problems/mend/

Given: A rooted binary tree TT in Newick format encoding an individual's
pedigree for a Mendelian factor whose alleles are A (dominant) and a
(recessive).

Return: Three numbers between 0 and 1, corresponding to the respective
probabilities that the individual at the root of TT will exhibit the
"AA", "Aa" and "aa" genotypes.
"""


class Node(object):

    def __init__(self, genotype=None):
        self.genotype = genotype
        self.probability = dict(
            AA=1.0 if genotype == 'AA' else 0.0,
            Aa=1.0 if genotype == 'Aa' else 0.0,
            aa=1.0 if genotype == 'aa' else 0.0,
        ) if genotype else None
        self.parent = None
        self.left = None
        self.right = None

    def calc_probability(self):
        if not self.left.probability:
            self.left.calc_probability()
        if not self.right.probability:
            self.right.calc_probability()

        l = self.left.probability
        r = self.right.probability
        AA = l['AA']*r['AA'] + l['AA']*r['Aa']*0.5 + l['Aa']*r['AA']*0.5 + l['Aa']*r['Aa']*0.25
        Aa = l['AA']*r['Aa']*0.5 + l['AA']*r['aa'] + l['Aa']*r['AA']*0.5 + l['Aa']*r['Aa']*0.5 + l['Aa']*r['aa']*0.5 + l['aa']*r['AA'] + l['aa']*r['Aa']*0.5
        aa = l['Aa']*r['Aa']*0.25 + l['Aa']*r['aa']*0.5 + l['aa']*r['Aa']*0.5 + l['aa']*r['aa']

        self.probability = dict(AA=AA, Aa=Aa, aa=aa)

    def set_child(self, direction, node):
        node.parent = self
        setattr(self, direction, node)


def build_tree(newick_str):
    newick_str = newick_str.strip().replace(';', '')[1:-1]
    current_node = Node()
    genotype = ''
    direction = 'left'

    for s in newick_str:
        if s.isalpha() and len(genotype) == 0:
            genotype = s
        elif s.isalpha() and len(genotype) == 1:
            genotype += s
            current_node.set_child(direction, Node(genotype))
            genotype = ''
        elif ',' == s:
            direction = 'right'
        elif '(' == s:
            new_node = Node()
            current_node.set_child(direction, new_node)
            current_node = new_node
            direction = 'left'
        elif ')' == s:
            current_node = current_node.parent

    return current_node


def main(newick_str):
    """
    >>> main('((((Aa,aa),(Aa,Aa)),((aa,aa),(aa,AA))),Aa);')
    (0.156, 0.5, 0.344)
    """
    root = build_tree(newick_str)
    root.calc_probability()
    return root.probability


if __name__ == '__main__':
    probability = main('((((Aa,aa),(Aa,Aa)),((aa,aa),(aa,AA))),Aa);')
    print('{AA} {Aa} {aa}'.format(**probability))
