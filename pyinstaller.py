import numpy as np
import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem
from rdchiral.main import RDChiralReaction, RDChiralRunText
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense



def reaction_to_fingerprint(reaction_smarts, fp_size=2048):
    rxn = RDChiralReaction(reaction_smarts)
    reactants, products = rxn.get_reactants(), rxn.get_products()
    reactants_fp = sum(AllChem.GetMorganFingerprintAsBitVect(m, 2, nBits=fp_size) for m in reactants)
    products_fp = sum(AllChem.GetMorganFingerprintAsBitVect(m, 2, nBits=fp_size) for m in products)
    return reactants_fp, products_fp

def fingerprint_to_reaction(reactants_fp, products_fp, fp_size=2048):
    reactants = [Chem.MolFromSmiles('C')]
    products = [Chem.MolFromSmiles('C')]
    
    for i in range(fp_size):
        if reactants_fp[i]:
            reactants.append(Chem.MolFromSmiles('*'))
        if products_fp[i]:
            products.append(Chem.MolFromSmiles('*'))
    
    return RDChiralReaction('>>'.join([Chem.MolToSmarts(m) for m in reactants]) + '>>' + '>>'.join([Chem.MolToSmarts(m) for m in products]))

# Carga tus datos de reacciones aquí (en formato SMARTS)
reactions_data = []  # Lista de SMARTS de reacciones

# Convierte las reacciones en fingerprints
reactants_fps, products_fps = zip(*[reaction_to_fingerprint(rxn) for rxn in reactions_data])

X = np.array(reactants_fps)
y = np.array(products_fps)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Define la arquitectura de la red neuronal
model = Sequential()
model.add(Dense(512, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(y_train.shape[1
