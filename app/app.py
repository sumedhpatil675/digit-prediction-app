# app.py

from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io
import base64
import mysql.connector

app = Flask(__name__)

# Load the saved model
model = load_model('models/mnist_model.h5')


# Function to establish a database connection
def get_db_connection():
    try:
        db = mysql.connector.connect(
            host="mysql-db",
            user="root",
            password="password",
            database="prediction_db"
        )
        print("Database connection successful")
        return db
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Function to close the database connection
def close_db_connection(db, cursor):
    if cursor:
        cursor.close()
    if db and db.is_connected():
        db.close()
        print("Database connection closed")

# Create a table for storing predictions
def create_predictions_table(cursor):
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS predictions (id INT AUTO_INCREMENT PRIMARY KEY, image_path VARCHAR(255), prediction INT)")
        print("Table created successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Function to save a prediction to the database
def save_to_database(image_path, prediction, db, cursor):
    try:
        prediction = int(prediction)
        cursor.execute("INSERT INTO predictions (image_path, prediction) VALUES (%s, %s)", (image_path, prediction))
        db.commit()
        print("Record inserted successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")


db = get_db_connection()
if db is None:
    print("not connected")
    # return jsonify({'error': 'Unable to connect to the database'})
else:
    print("connected")
    
cursor = db.cursor()
create_predictions_table(cursor)


def preprocess_image(file):
    img = Image.open(file).convert('L')  # Convert to grayscale
    img = img.resize((28, 28))
    img_array = np.array(img).reshape(28, 28, 1)
    img_array = img_array / 255.0
    return img_array

def preprocess_image_from_base64(encoded_image):
    # Decode base64 and process the image
    decoded_image = io.BytesIO(base64.b64decode(encoded_image))
    img = Image.open(decoded_image).convert('L')  # Convert to grayscale
    img = img.resize((28, 28))
    img_array = np.array(img).reshape(28, 28, 1)
    img_array = img_array / 255.0
    return img_array

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     if request.method == 'POST':
#         # Check if the post request has the file part
#         if 'file' not in request.files:
#             return render_template('index.html', error='No file part')

#         file = request.files['file']

#         # If the user does not select a file, submit an empty part without filename
#         if file.filename == '':
#             return render_template('index.html', error='No selected file')

#         try:
#             image_data = preprocess_image(file)
#         except Exception as e:
#             return render_template('index.html', error=f'Error processing image: {str(e)}')

#         predictions = model.predict(np.array([image_data]))
#         predicted_label = np.argmax(predictions[0])

#         return render_template('index.html', prediction=predicted_label)

@app.route('/api/predict', methods=['POST'])
def api_predict():

    
    if request.method == 'POST':
        # file = request.files['file']

        # if file.filename == '':
        #     return render_template('index.html', error='No selected file')
        
        try:
            data = request.json
            image_data = preprocess_image_from_base64(data['image'])
            file_name = data['file_name']
        except Exception as e:
            # close_db_connection(db, cursor)
            return jsonify({'error': f'Error processing image: {str(e)}'})

        predictions = model.predict(np.array([image_data]))
        predicted_label = np.argmax(predictions[0])
        save_to_database(file_name, predicted_label, db, cursor)

        # close_db_connection(db, cursor)

        return jsonify({'prediction': int(predicted_label)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80,debug=True)