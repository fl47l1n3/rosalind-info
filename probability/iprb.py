"""
http://rosalind.info/problems/iprb/

Given: Three positive integers kk, mm, and nn, representing a population
containing k+m+nk+m+n organisms: kk individuals are homozygous dominant for a
factor, mm are heterozygous, and nn are homozygous recessive.

Return: The probability that two randomly selected mating organisms will
produce an individual possessing a dominant allele (and thus displaying the
dominant phenotype). Assume that any two organisms can mate.
"""

from __future__ import division
import sys


def calc_probability_dominant_allele(d, h, r):
    population = d + h + r
    prob_d = d / population
    prob_h_d = h / population * d / (population - 1)
    prob_h_h = h / population * (h - 1) / (population - 1) * 0.75
    prob_h_r = h / population * r / (population - 1) * 0.5
    prob_r_d = r / population * d / (population - 1)
    prob_r_h = r / population * h / (population - 1) * 0.5
    return prob_d + (prob_h_d + prob_h_h + prob_h_r) + (prob_r_d + prob_r_h)


if __name__ == '__main__':
    data = sys.stdin.readline().split()
    r = calc_probability_dominant_allele(
        int(data[0]), int(data[1]), int(data[2])
    )
    print(r)
