import itertools

print('1 millionth permutation:',''.join(list(itertools.permutations('0123456789',10))[1000000-1]))
