import datetime as dt

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


def print_world():
    print('world')

def print_execution_date(**context):
    execution_date = context['execution_date']
    print(f"Execution date is : {execution_date}")

default_args = {
    'owner': 'me',
    'start_date': dt.datetime(2023, 11, 24),
    'retries': 10,
    'retry_delay': dt.timedelta(minutes=5),
}


with DAG(dag_id='airflow_tutorial_v01',
        default_args=default_args,
        schedule_interval='0 * * * *',
        catchup=False
         ) as dag:

    print_hello = BashOperator(task_id='print_hello',
                               bash_command='echo print_execution_date'
                               )
    sleep = BashOperator(task_id='sleep',
                         bash_command='sleep 10')
    print_world = PythonOperator(task_id='print_world',
                                 python_callable=print_world)


print_hello >> sleep >> print_world