dna_rna = {'A': 'U',
           'C': 'G',
           'T': 'A',
           'G': 'C'}
dna = input()
res = [dna_rna[key] for key in dna]
print(''.join(res))
