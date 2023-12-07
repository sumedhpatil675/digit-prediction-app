Structure of our app
-------------------------

Our project will consist app, mysql directory


app/ -
This directory will consist of directories models,templates and files 
app.py, create_and_train_model.py, Dockerfile and requirements.txt file

  app.py 
  -----------------------

  This file will be starting point of our application. It will take care of rendering homepage. i.e index.html

  It also contains a code for /predict api with mannaging connection with mysql db also insertion of prediction result in mysql db.

  This prediction will done based on mnist_model.h5 file which we loaded initially at the start of our application.


  create_and_train_model.py
  -------------------------

    1 . Loading and Preprocessing Data:

    It loads the MNIST dataset using TensorFlow's mnist.load_data() function.
    The pixel values of the images are normalized to the range [0, 1] by dividing them by 255.
    The dataset is reshaped to have a single channel (as it is grayscale).


    2 . Defining the Model:

    It defines a convolutional neural network (CNN) model using TensorFlow's Keras API.
    The model consists of a convolutional layer with 32 filters, each of size (3, 3) and using the ReLU activation function.
    It includes a max-pooling layer to down-sample the spatial dimensions.
    The data is then flattened and passed through a dense layer with 10 units and a softmax activation function, suitable for multi-class classification (MNIST has 10 classes).

    3 . Compiling the Model:

    The model is compiled with the Adam optimizer, sparse categorical crossentropy loss (appropriate for integer labels like in MNIST), and accuracy as the evaluation metric.

    4 . Training the Model:

    The model is trained using the training images and labels.
    The training is performed for 5 epochs, and validation data (from the test set) is used to evaluate the model's performance during training.
    Saving the Trained Model:

    After training, the script saves the trained model in the Hierarchical Data Format version 5 (HDF5) file format with the filename 'mnist_model.h5'. The model can be later loaded for inference without retraining.

  Dockerfile
  ---------------------------

  - It uses the latest TensorFlow base image.
  - Sets the working directory to /app.
  - Copies application files into the container.
  - Installs system dependencies for Pillow (image processing library).
  - Installs Python dependencies from requirements.txt.
  - Installs the MySQL Connector Python library.
  - Exposes port 80 (documentation purpose).
  - Specifies that the default command to run is python app.py when the container starts.

  requirements.txt
  ---------------------------
  It will contain all the dependencies required for this project.



  models/mnist_model.h5
  ----------------------------
  This will contain model file, which will used to predict the result.

  templates/index.html
  ----------------------------
  Its homepage of our application , it will consist of html,javascript code for rendering file uploading functionallity also javascript code for hitting /predict api



Steps for Starting Applications
======================================


1. Install required depedencies

First go to app folder, and type command

pip install -r requirements.txt

This will install all the libraries required for project.





3. Start our application

  1. Using docker-compose

       1. To start application using docker-compose we can use command
        - docker-compose up --build

          This will create a docker container for prediction app and mysql and run starting files of the containers. i.e create_and_train_model.py and app.py

        
       2. create_and_train_model.py
        will create a mnist_model.h5 model file in models directory. Which we will use in our /predict api for result prediction.
        

       3. Then you can access our app using below url
            Type below url in your browser and press enter
            - localhost

   2. Using kubernetes
        1. Start kubernetes clusters
        - kubectl apply -f digit-prediction-app-deployment.yaml  
        - kubectl apply -f mysql-deployment.yaml

         These commands will deploy two different components (a digit prediction application and a MySQL database) to a Kubernetes cluster by applying their respective YAML configurations.

        2. Accessing the application
         
         Type below url in your browser and press enter
            - localhost