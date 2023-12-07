import uuid
import airflow

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator

def _train_model(**context):
    model_id = str(uuid.uuid4())
    return model_id

def _deploy_model(templates_dict, **context):
    model_id = templates_dict["model_id"]
    print(f"Deployinbg model {model_id}")

with DAG(
    dag_id="11_xcom_templates",
    start_date=airflow.utils.dates.days_ago(3),
    schedule_interval="@daily",
) as dag:
    start = DummyOperator(task_id="start")

    fetch_sales = DummyOperator(task_id="fetch_sales")
    clean_sales = DummyOperator(task_id="clean_sales")

    fetch_weather = DummyOperator(task_id="fetch_weather")
    clean_weather = DummyOperator(task_id="clean_weather")

    join_dastasets = DummyOperator(task_id="join_dastasets")

    train_model = PythonOperator(task_id="train_model", python_callable=_train_model)

    deploy_model = PythonOperator(
        task_id="deploy_model",
        python_callable=_deploy_model,
        templates_dict={
            "model_id": "{{task_instance.xcom_pull(task_ids='train_model', key='model_id')}}"
        },
    )

    start >> [fetch_sales, fetch_weather]
    fetch_sales >> clean_sales
    fetch_weather >> clean_weather
    [clean_sales, clean_weather] >> join_dastasets
    join_dastasets >> train_model >> deploy_model