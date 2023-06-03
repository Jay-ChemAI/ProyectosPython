import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from rdkit import Chem
from sklearn.model_selection import train_test_split
from rdkit.Chem import AllChem


data = [ "C1CCC(CC1)NC2=NC(C3=CC=CO3)=C4C=CN=CC4=N2", # N-cyclohexyl-2-(furan-2-yl)imidazo[1,2-a]pyridin-3-amine 
"C1CCC(CC1)NC2=NC(Cl)=C3C=CN=CC3=C2C4=CC=CO4", #6-chloro-N-cyclohexyl-2-(furan-2-yl)imidazo[1,2-a]pyridin-3-amine
"COC(=O)C1=NC(C2=CC=CO2)=C3C=CN=CC3=C1NC4CCCCC4", #3-(cyclohexylamino)-2-(furan-2-yl)imidazo[1,2-a]pyridine-7-carboxylate
"C1CCC(CC1)NC2=NC(C3=CC=CO3)=C4C=CN=CC4=C2C#N", # 3-(cyclohexylamino)-2-(furan-2-yl)imidazo[1,2-a]pyridine-6-carbonitrile
"COc1ccc(NC2=NC(C3=CC=CO3)=C4C=CN=CC4=N2)cc1" # 2-(furan-2-yl)-N-(4-methoxyphenyl)imidazo[1,2-a]pyridin-3-amine
"COc1ccc(NC2=NC(Cl)=C3C=CN=CC3=C2C4=CC=CO4)cc1" #6-chloro-2-(furan-2-yl)-N-(4-methoxyphenyl)imidazo[1,2-a]pyridin-3-amine
"COC(=O)C1=NC(C2=CC=CO2)=C3C=CN=CC3=C1NC4=CC=C(C=C4)OC" # methyl 2-(furan-2-yl)-3-((4-methoxyphenyl)amino)imidazo[1,2-a]pyridine-7-carboxylate
"COc1ccc(NC2=NC(C3=CC=C(C)O3)=C4C=CN=CC4=C2C#N)cc1" # 3-((4-methoxyphenyl)amino)-2-(5-methylfuran-2-yl)imidazo[1,2-a]pyridine-6-carbonitrile
"COC(=O)C1=NC(C2=CC=C(C)O2)=C3C=CN=CC3=C1NC4=CC=C(C=C4)OC" #3-((4-methoxyphenyl)amino)-2-(5-methylfuran-2-yl)imidazo[1,2-a]pyridine-7-carboxylate
]
X_train, X_val = train_test_split(data, test_size=0.2, random_state=42)

# Tokenizar las cadenas SMILES y convertirlas en secuencias numéricas
tokenizer = Tokenizer(char_level=True)
tokenizer.fit_on_texts(X_train)

X_train_seq = tokenizer.texts_to_sequences(X_train)
X_val_seq = tokenizer.texts_to_sequences(X_val)

# Rellenar las secuencias para que tengan la misma longitud
max_sequence_length = max([len(seq) for seq in X_train_seq])
X_train_padded = pad_sequences(X_train_seq, maxlen=max_sequence_length, padding='post')
X_val_padded = pad_sequences(X_val_seq, maxlen=max_sequence_length, padding='post')

# Codificar one-hot las secuencias
num_tokens = len(tokenizer.word_index) + 1
X_train_one_hot = to_categorical(X_train_padded, num_classes=num_tokens)
X_val_one_hot = to_categorical(X_val_padded, num_classes=num_tokens)

# Preparar las etiquetas para la red neuronal (desplazadas un paso hacia adelante en el tiempo)
y_train_padded = np.hstack([X_train_padded[:, 1:], np.zeros((X_train_padded.shape[0], 1))])
y_val_padded = np.hstack([X_val_padded[:, 1:], np.zeros((X_val_padded.shape[0], 1))])

y_train_one_hot = to_categorical(y_train_padded, num_classes=num_tokens)
y_val_one_hot = to_categorical(y_val_padded, num_classes=num_tokens)

# Definir el modelo
model = Sequential()
model.add(LSTM(128, input_shape=(max_sequence_length, num_tokens), return_sequences=True))
model.add(Dense(num_tokens, activation='softmax'))
model.compile(optimizer=Adam(learning_rate=0.001), loss='categorical_crossentropy')

# Entrenar el modelo
model.fit(X_train_one_hot, y_train_one_hot, validation_data=(X_val_one_hot, y_val_one_hot), epochs=20, batch_size=64)

def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

def generate_smiles(model, tokenizer, start_seq, max_sequence_length, max_len=100, temperature=1.0):
    generated_seq = start_seq
    token_index = tokenizer.word_index
    index_token = dict((i, c) for c, i in token_index.items())

    while True:
        # Convertir la secuencia actual en una secuencia de índices numéricos y rellenarla
        seq_indices = tokenizer.texts_to_sequences([generated_seq])
        seq_padded = pad_sequences(seq_indices, maxlen=max_sequence_length, padding='post')

        # Convertir la secuencia rellenada en una representación one-hot
        seq_one_hot = to_categorical(seq_padded, num_classes=len(token_index) + 1)

        # Predecir el siguiente carácter
        preds = model.predict(seq_one_hot)[0][-1]
        next_index = sample(preds, temperature)
        next_token = index_token.get(next_index)

        # Detener la generación si se encuentra un carácter de finalización o se alcanza la longitud máxima
        if next_token is None or len(generated_seq) + 1 > max_len:
            break

        # Agregar el siguiente carácter a la secuencia
        generated_seq += next_token

    return generated_seq

# Generar una nueva cadena SMILES
start_sequence = "C"  # puedes elegir cualquier secuencia de inicio válida
generated_smiles = generate_smiles(model, tokenizer, start_sequence, max_sequence_length)
print("Generated SMILES:", generated_smiles)

'''
# Convertir la cadena SMILES en una estructura molecular
mol = Chem.MolFromSmiles(generated_smiles)

if mol is not None:
    # Asegurarse de que la molécula tenga coordenadas 3D
    AllChem.Compute2DCoords(mol)

    # Guardar la molécula en un archivo .mol
    with open("output.mol", "w") as f:
        f.write(Chem.MolToMolBlock(mol))
    print("Molecule saved to output.mol")
else:
    print("Generated SMILES is not valid.")
'''