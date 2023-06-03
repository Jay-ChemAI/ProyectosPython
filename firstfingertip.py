from rdkit import Chem
from rdkit.Chem import AllChem

ncy = Chem.MolFromSmiles("C1CCC(CC1)NC2=NC(C3=CC=CO3)=C4C=CN=CC4=N2")
mol_block = Chem.MolToMolBlock(ncy)

with open("ncyclo.mol", "w") as f:
    f.write(mol_block)
