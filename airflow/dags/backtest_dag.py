from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import requests
import json

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Initialize the DAG
dag = DAG(
    'backtest_dag',
    default_args=default_args,
    description='A simple DAG to run backtests',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    catchup=False,
)

# Define the Python function to run the backtest
def run_backtest():
    url = 'http://localhost:5000/run_backtest'
    headers = {'Content-Type': 'application/json'}
    payload = {
        "scene_name": "example_scene",
        "params": {
            "start_date": "2023-01-01",
            "end_date": "2023-12-31",
            "indicator": "sma",
            "indicator_params": {"window": 10}
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        print('Backtest completed successfully')
        print('Results:', response.json())
    else:
        print('Failed to run backtest')
        print('Response:', response.text)

# Create the PythonOperator to run the backtest
run_backtest_task = PythonOperator(
    task_id='run_backtest',
    python_callable=run_backtest,
    dag=dag,
)

# Define the task dependencies
run_backtest_task
