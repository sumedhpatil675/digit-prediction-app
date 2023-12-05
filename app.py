# app.py

from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

# Load the saved model
model = load_model('models/mnist_model.h5')

def preprocess_image(file):
    img = Image.open(file).convert('L')  # Convert to grayscale
    img = img.resize((28, 28))
    img_array = np.array(img).reshape(28, 28, 1)
    img_array = img_array / 255.0
    return img_array

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return render_template('index.html', error='No file part')

        file = request.files['file']

        # If the user does not select a file, submit an empty part without filename
        if file.filename == '':
            return render_template('index.html', error='No selected file')

        try:
            image_data = preprocess_image(file)
        except Exception as e:
            return render_template('index.html', error=f'Error processing image: {str(e)}')

        predictions = model.predict(np.array([image_data]))
        predicted_label = np.argmax(predictions[0])

        return render_template('index.html', prediction=predicted_label)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
