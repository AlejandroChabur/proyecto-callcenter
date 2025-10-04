from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

# Configuración por defecto del DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 10, 1),
    'retries': 1
}

# Funciones que llaman a los scripts
def load_initial():
    os.system("python /opt/airflow/dags/scripts/load_initial_data.py")

def insert_new():
    os.system("python /opt/airflow/dags/scripts/insert_new_data.py")

# Definir DAG
with DAG("callcenter_pipeline",
         default_args=default_args,
         schedule_interval="@daily",   # se ejecuta 1 vez al día
         catchup=False) as dag:

    carga_inicial = PythonOperator(
        task_id="carga_inicial",
        python_callable=load_initial
    )

    insertar_nuevos = PythonOperator(
        task_id="insertar_nuevos",
        python_callable=insert_new
    )

    # La primera vez corre carga_inicial, luego siempre insertar_nuevos
    carga_inicial >> insertar_nuevos
