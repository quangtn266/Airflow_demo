# Airflow_demo
Demo code for Airflow. (Data Pipeline with Apache Airflow).

# Commands for local machine (Terminal) without container (Optional)

1.  export AIRFLOW_HOME=/Users/quangtn/Desktop/01_work/01_job/Source/data_course/airflow
2.  airflow db init (reset)
3.  airflow users create --username admin --password admin --firstname Quang --lastname Admin --role Admin --email quangtn933@gmail.com
4. airflow webserver -p 8080
5. airflow scheduler
6.  airflow connections add --conn-type postgres --conn-host localhost --conn-login postgres --conn-password mysecretpassword my_postgres
    1. airflow connections add --conn-type postgres --conn-host localhost --conn-login postgres postgres

Chapter 10: I modify docker-compose.yml file to adapt airflow version (2.7.3).

- AIRFLOW_HOME=/opt/airflow

- AIRFLOW__CORE__ENABLE_XCOM_PICKLING=True

1) Docker.
2) Kubernetes.

## Docker:
1) docker-compose up -d --build
2) docker-compose down -v
