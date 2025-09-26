def reverse_complement(seq):
    complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return ''.join(complement.get(base, base) for base in reversed(seq.upper()))
