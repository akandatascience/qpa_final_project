from models import Base, engine, RNA, DNA, Codon, Amino_Acid, Session
s = Session()

def create_database():
    Base.metadata.create_all(engine)
create_database()



rna_a = RNA(name = "A")
rna_u = RNA(name = "U")
rna_c = RNA(name = "C")
rna_g = RNA(name = "G")


dna_a = DNA(name = "A", rna_base = rna_a)
dna_t = DNA(name = "T", rna_base = rna_u)
dna_c = DNA(name = "C", rna_base = rna_c)
dna_g = DNA(name = "G", rna_base = rna_g)
dna_bases = [dna_a,dna_t,dna_c,dna_g]


s.add_all(dna_bases)


codon_table = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
     "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
     "UAU":"Y", "UAC":"Y", "UAA":".", "UAG":".",
     "UGU":"C", "UGC":"C", "UGA":".", "UGG":"W",
     
     "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
     "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
     "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
     "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
     
     "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
     "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
     "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
     "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
     
     "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
     "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
     "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
     "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",
    }



for codon, amino_acid in codon_table.items():
    aa = Amino_Acid(name = amino_acid)
    codon_item = Codon(name = codon,amino_acid=aa)
    s.add(codon_item)

s.commit()
s.close()
           




