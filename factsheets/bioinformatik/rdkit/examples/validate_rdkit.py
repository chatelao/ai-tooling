from rdkit import Chem
mol = Chem.MolFromSmiles('CCO')
print(Chem.MolToMolBlock(mol))