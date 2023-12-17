# Airflow_demo
Demo code for Airflow. (Data Pipeline with Apache Airflow).

The demo code for chapter 12 will show you a basic architect when Airflow is applied in production.

## The structure code includes:
- Airflow.
- Redis.
- Prometheus.
- Grafana
- Docker-compose.

## Steps:
1. docker-compose up -d (localhost:8080)
2. docker-compose down -v

## Note for the chapter.
In Airflow, there are 4 kinds of executor:
1. Sequential Executor.
2. Local Executor
3. Celery Executor
4. Kuebernestes Executor
