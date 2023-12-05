# ai_task


docker build -t my-flask-app .

docker run -p 4000:80 my-flask-app

docker exec -it 65e22e3af53c /bin/bash



Apply Kubernetes Manifests:

Apply the Deployment and Service YAML files to your Kubernetes cluster:

-----------------------------------------------
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
-----------------------------------------------



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



