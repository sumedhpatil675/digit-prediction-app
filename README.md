# ai_task


docker build -t my-flask-app .

docker run -p 4000:80 my-flask-app

docker exec -it 65e22e3af53c /bin/bash


Deploy kubenetes 
==========================
kubectl apply -f digit-prediction-app-deployment.yaml  
kubectl apply -f digit-prediction-app-service.yaml
kubectl apply -f mysql-deployment.yaml





Access the Application:

Check the status of your Deployment:

----------------------------------------
kubectl get pods
----------------------------------------


Once the pod is running, get the URL to access your application:

----------------------------------------
kubectl get services
----------------------------------------


Look for the EXTERNAL-IP of your service. If it's pending, wait for it to get an external IP (this might take a minute).

Open your web browser and access the application using the external IP and port 80.

Cleanup:

When you're done, you can delete the resources:

--------------------------------------------------
kubectl delete deployment digit-prediction-app
kubectl delete service digit-prediction-app-service
--------------------------------------------------


This should get your Flask application running on Kubernetes using Docker Desktop. If you face any issues, check the logs and describe the pods and services for more 






to build the digit-prediction-app localy
============================================

docker build --no-cache -t sumedhpatil675/digit_prediction:latest .


docker push sumedhpatil675/digit_prediction:latest


to expose digit-prediction-app-service  to port 8080
=============================================
kubectl port-forward service/digit-prediction-app-service 8080:80


to acces docker mysql using kubectl
===================================

kubectl exec -it mysql-78d67b4567-4w522 -- /bin/bash

Replace <your-pod-id> with the actual identifier of your MySQL pod. You can find the pod ID using the kubectl get pods command.

Once you are inside the MySQL container, you can use the mysql command to access the MySQL client:

============================================
mysql -u root -p
============================================


Enter the MySQL root password when prompted.

After entering the MySQL client, switch to the prediction_db database:

============================================
USE prediction_db;
============================================

Query the predictions table:

============================================
SELECT * FROM predictions;
============================================


It seems like there's an issue with the code formatting. If you're trying to run MySQL and Flask containers in the same Docker network, you can follow these steps:

Create a Docker network:

=============================================
docker network create my_network
=============================================


Run MySQL container and connect it to the network:

=============================================
docker run --name mysql-container --network my_network -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=prediction_db -d mysql:latest
=============================================


Run Flask container and connect it to the network. Make sure to replace /path/to/models, /path/to/templates, and /path/to/app with the actual paths on your local machine:

=============================================
docker run --name digit-prediction-app-container --network my_network -p 80:80 -v models:/app/models -v templates:/app/templates -v app:/app digit_prediction:latest
=============================================


This assumes that you have built a Docker image for your Flask app with the tag flask-app:latest. Adjust the image name accordingly based on how you've tagged your Flask app image.