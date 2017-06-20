"""
Convert DNA to RNA
"""

def rna(seq):
    """Convert DNA to RNA"""
    #determine if seq is uppercase
    seq_upper = seq.isupper()

    #convert to lower complement_base
    seq = seq.lower()
    seq = seq.replace('t','u')

    #return upper of lower, depending on input
    if seq_upper:
        return seq.upper()
    else:
        return seq

def reverse_rna_compl(seq):
    """conver DNA to reverse complement RNA"""

    #determine if original seq is uppercase
    seq_upper = seq.isupper()

    #reverse original sequence
    seq = seq[::-1]

    #convert to uppercase
    seq = seq.upper()

    #compute complement_base
    seq = seq.replace('A','u')
    seq = seq.replace('T','a')
    seq = seq.replace('G','c')
    seq = seq.replace('C','g')

    #return in appropriate complement_base
    if seq_upper:
        return seq.upper()
    else:
        return seq
