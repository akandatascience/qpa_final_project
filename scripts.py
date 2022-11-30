from data.retrieveing_data import *

rna_map =  get_rna_map()
codon_map = get_codons_map()

def convert_dna_to_rna(sequence: str) ->str:
    new_string = ""
    for i in sequence:
            new_string += rna_map[i]
    return new_string

def convert_rna_to_protein(sequence: str) ->str:
    
    new_string = ""
    k=3
    temp=""
    start=0
    size = len(sequence)//3
    for i in range(1,size+1):
        temp = sequence[start:i*k]
        new_string+=codon_map[temp]
        start+=3
    return new_string
        