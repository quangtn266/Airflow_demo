# Airflow_demo
Demo code for Airflow. (Data Pipeline with Apache Airflow).

The demo code will cover programming code for the book following each chapter.

## Running k8s.
I run the code by using Minikube. (https://minikube.sigs.k8s.io/docs/start/). To start/ stop minikube, you can follow the commands:
1. minikube start
2. minikube stop
3. minikube dashboard (it's optional, if you want o check current status)

To run the code, you should follow the steps:
1. kubectl create namespace airflow (To create a namespace)
2. kubectl --namespace airflow apply -f resources/data-volume.yml (To create a PesistentVolume)
3. docker build -t manning-airflow/movielens-api ../chapter08/docker/movielens-api
4. kubectl --namespace airflow apply -f resources/api.yml (To deploy API)
5. kubectl --namespace airflow port-forward svc/movielens 8000:80 (To test the service)

Besides, you also run other method with docker-compose.
1. docker-compose up

# Note:
You can meet some error during docker build because the pod from k8s will show an error ("ErrImageNeverPull"). There are some notes to do:
1. Delete redundant image in Docker desktop.
2. you should fix error from Docker file.
3. Ignore error by adding " || true " in the line of error.
