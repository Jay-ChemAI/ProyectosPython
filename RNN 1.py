import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, LSTM, Activation
from keras.optimizers import Adam
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

# Carga tus datos SMILES aquí
smiles_data = ['c1ccccc1', 'CC(=O)O', ...] # Reemplaza esto con tus propias cadenas SMILES

tokenizer = Tokenizer(char_level=True)
tokenizer.fit_on_texts(smiles_data)
encoded_smiles = tokenizer.texts_to_sequences(smiles_data)

max_length = max([len(smile) for smile in encoded_smiles])
vocab_size = len(tokenizer.word_index) + 1

padded_smiles = pad_sequences(encoded_smiles, maxlen=max_length, padding='post')


X = padded_smiles[:, :-1]
y = padded_smiles[:, 1:]

y = keras.utils.to_categorical(y, num_classes=vocab_size)


model = Sequential()
model.add(LSTM(128, input_shape=(X.shape[1], vocab_size), return_sequences=True))
model.add(Dense(vocab_size))
model.add(Activation('softmax'))

model.compile(optimizer=Adam(lr=0.001), loss='categorical_crossentropy')

model.fit(X, y, epochs=50, batch_size=32, validation_split=0.1)
