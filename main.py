import numpy as np
import tensorflow as tf
import random
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Activation
from tensorflow.keras.optimizers import RMSprop

# Load and preprocessing text
filepath = tf.keras.utils.get_file('shakespeare.txt', 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(filepath, 'rb').read().decode(encoding='utf-8').lower()
text = text[300000:800000]

# Character mapping
characters = sorted(set(text))
char_to_index = {c: i for i, c in enumerate(characters)}
index_to_char = {i: c for i, c in enumerate(characters)}

# Creating sequences
SEQ_LENGTH = 40
STEP_SIZE = 3

# --- Training Section (Remove comments to run this section) ---
'''

sentences = []
next_characters = []

for i in range(0, len(text) - SEQ_LENGTH, STEP_SIZE):
    sentences.append(text[i: i + SEQ_LENGTH])
    next_characters.append(text[i + SEQ_LENGTH])


x = np.zeros((len(sentences), SEQ_LENGTH, len(characters)), dtype=bool)
y = np.zeros((len(sentences), len(characters)), dtype=bool)



for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        x[i, t, char_to_index[char]] = 1
    y[i, char_to_index[next_characters[i]]] = 1

# Building the model
model = Sequential()
model.add(LSTM(128, input_shape=(SEQ_LENGTH, len(characters))))
model.add(Dense(len(characters)))
model.add(Activation('softmax'))

# Compiling the model
model.compile(loss='categorical_crossentropy', optimizer=RMSprop(learning_rate=0.01))

# The model will be trained
model.fit(x, y, batch_size=256, epochs=4)

# Saving the model
model.save('textgenerator.keras')

'''
# Load the trained model
model = tf.keras.models.load_model('textgenerator.keras')

# Sampling function
def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds + 1e-8) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

    # Text generation function
def generating_text(length, temperature):
    start_index = random.randint(0, len(text) - SEQ_LENGTH - 1)
    sentence = text[start_index: start_index + SEQ_LENGTH]
    generated = sentence

    for i in range(length):
        x = np.zeros((1, SEQ_LENGTH, len(characters)))
        for t, character in enumerate(sentence):
            x[0, t, char_to_index[character]] = 1

        predictions = model.predict(x, verbose=0)[0]
        next_index = sample(predictions, temperature)
        next_character = index_to_char[next_index]

        generated += next_character
        sentence = sentence[1:] + next_character

    return generated


print('.........0.2.............')
print(generating_text(300, 0.2))
print('.........0.4.............')
print(generating_text(300, 0.4))
print('.........0.6.............')
print(generating_text(300, 0.6))
print('.........0.8.............')
print(generating_text(300, 0.8))
print('.........0.8.............')
print(generating_text(300, 0.8))
print('.........1.............')
print(generating_text(300, 1.0))

