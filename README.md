# Generating Poetic Text with Recurrent Neural Networks with Python

This project demonstrates how to generate a poetic text using a Recurrent Neural Network (RNN) with Long Short-Term Memory (LSTM) layers in Python. It is trained on Shakespeare's work to produce stylistically similar text with adjustable creativity.

### Project Structure

Poetic_Texts_Neural_Networks/

├── main.py                 
├── textgenerator.Keras      
├── README.md             
└── (optional) venv/     

### Feature    

The program loads and preprocesses real Shakespearean text, which is then used to train an LSTM model to predict the next character. When completed, it generates text with varying creativity using temperature-based sampling. Finally, it saves and reuses trained models for future predictions.

### AI & Model Overview 

The project uses Artificial Intelligence to generate text inspired by Shakespeare. It uses an LSTM-based Recurrent Neural Network, which is ideal for learning from sequences of characters.

Application Key Concepts 
Training Data: A selection of Shakespeare's writing (downloaded from TensorFlow Datasets).
Text Preprocessing: The text is converted to lowercase and sliced into character-based sequences to train the model.
Neural Network: The model is a Sequential LSTM with a softmax output layer that predicts the next character in a sequence.
Temperature Sampling: To generate text, a temperature-controlled sampling function influences the randomness and creativity of the output.

### Why LSTM?

LSTM cells help preserve the context over long sequences, making them ideal for poetic or structured language generation where previous characters strongly influence the next.

### Running the Application
Install the dependencies (pip install tensorflow numpy) if not already installed.
If you choose to run the trained model and not use the already trained model, which is saved as textgenerator.keras, please remove the code which is comments, e.g. # --- Training Section (Remove comments to run this section) ---
Finally run the main.py.
 Suppose you have chosen to train the model. Please rerun the application with the training section commented on to generate text.
Please be aware that if you choose to train the model, the time it takes will depend on your hardware. 

### License 
This project is licensed under the MIT License.

### Author
Joshua Taylor 

taylor.jw21@hotmail.com 

Feel free to reach out for collaboration or feedback!
