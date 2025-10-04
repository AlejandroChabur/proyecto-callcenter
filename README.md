# Proyecto Call Center - ETL y Análisis de Datos

Este proyecto implementa un **ETL (Extract, Transform, Load)** para datos de un Call Center, cargando información desde un CSV hacia una base de datos MySQL, con el objetivo de poder analizar métricas clave como llamadas entrantes, abandonadas, tiempo de espera y nivel de servicio. Además, está preparado para integrarse con **Airflow** para cargas automatizadas y generar dashboards en herramientas como Power BI.

---

## 📂 Estructura del proyecto

proyecto-callcenter/
│
├─ dags/ # DAGs de Airflow y scripts ETL
│ ├─ scripts/
│ │ ├─ load_initial_data.py # Carga inicial desde CSV a MySQL
│ │ └─ insert_new_data.py # Inserción de registros aleatorios para pruebas
│ └─ tus_dags_airflow.py # DAGs para automatizar cargas
│
├─ data/ # Datos de entrada (CSV de ejemplo)
│ └─ call_center_data.csv
│
├─ docker-compose.yml # Configuración de contenedores MySQL y Airflow
├─ requirements.txt # Librerías necesarias para correr los scripts
├─ .gitignore # Archivos a ignorar en Git
└─ README.md # Documentación del proyecto

---

## ⚙️ Requisitos

- Python 3.9+  
- MySQL 8.0+  
- Docker y Docker Compose (opcional para entorno reproducible)  
- Librerías Python (instalar con `pip`):

```bash
pip install -r requirements.txt
📊 Métricas y análisis posibles

Algunas métricas que puedes calcular desde MySQL:

Promedio de llamadas entrantes:

SELECT AVG(incoming_calls) FROM callcenter;


Número máximo y mínimo de llamadas abandonadas:

SELECT MAX(abandoned_calls), MIN(abandoned_calls) FROM callcenter;


Promedio de nivel de servicio:

SELECT AVG(service_level) FROM callcenter;


Días con abandonos por encima del promedio:

SELECT fecha, abandoned_calls
FROM callcenter
WHERE abandoned_calls > (SELECT AVG(abandoned_calls) FROM callcenter)
ORDER BY abandoned_calls DESC;
