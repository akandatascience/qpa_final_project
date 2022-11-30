from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, relationship,sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey


engine = create_engine("sqlite:///final_project.db", echo=True)
Base = declarative_base()


Session = sessionmaker(bind=engine)


class DNA(Base):
    __tablename__ = "dna_bases"
    __table_args__ = {"extend_existing": True}
    
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    rna_base_id = Column(Integer, ForeignKey("rna_bases.id"))
    rna_base = relationship("RNA", foreign_keys=[rna_base_id])
    
    def __repr__(self):
        return f"name: {self.name} / rna_base: {self.rna_base}"


class RNA(Base):
    __tablename__ = "rna_bases"
    __table_args__ = {"extend_existing": True}
    
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    
    def __repr__(self)->str:
        return f"name: {self.name}"

class Codon(Base):
    __tablename__ = "codons_table"
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    amino_acid_id = Column(Integer, ForeignKey("amino_table.id"))
    amino_acid = relationship("Amino_Acid",foreign_keys=[amino_acid_id])
       
    def __repr__(self):
        return f"name: {self.name} / amino_acid: {self.amino_acid}"
    
class Amino_Acid(Base):
    __tablename__ = "amino_table"
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    
    def __repr__(self):
        return f"name: {self.name}"