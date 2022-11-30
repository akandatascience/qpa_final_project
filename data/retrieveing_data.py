
rna_map = {}
codon_map = {}

def get_rna_map():

    from data.models import engine,  DNA, Codon,Session
    s = Session()
    dna_bases = s.query(DNA).all()
    for base in dna_bases:
        rna_map[base.name] = str(base.rna_base)[-1]
    s.close()
    return rna_map


def get_codons_map():

    from data.models import engine,  DNA, Codon,Session
    s = Session()
    codons = s.query(Codon).all()
    for i in codons:
        codon_map[i.name] = str(i.amino_acid)[-1]
    s.close()
    return codon_map


