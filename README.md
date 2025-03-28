# DOCUMENTACIÓN
![image](https://github.com/user-attachments/assets/f81ad245-d69f-4634-8e38-39c84682d528)
> [!NOTE]
> Aqui en este repositorio se encuentra la tarea del analisis de Netflix.

> [!Important]
> Cualquier duda, pregunta o comentario sobre este notebook, contactarme.

# Análisis de Dataset de Netflix
Este repositorio contiene un análisis detallado del dataset de Netflix, que incluye información sobre películas y series disponibles en la plataforma. El objetivo del proyecto es explorar y visualizar los datos para obtener insights sobre el contenido de Netflix.

## Descripción del Dataset
El dataset contiene las siguientes columnas:

- `show_id`: Identificador único del contenido.

- `type`: Tipo de contenido (Movie o TV Show).

- `title`: Título del contenido.

- `director`: Director del contenido.

- `cast`: Actores principales.

- `country`: País de producción.

- `date_added`: Fecha en que el contenido fue añadido a Netflix.

- `release_year`: Año de lanzamiento del contenido.

- `rating`: Clasificación por edad.

- `duration`: Duración (en minutos para películas o temporadas para series).

- `listed_in`: Géneros o categorías del contenido.

- `description`: Descripción del contenido.



## Objetivos del Proyecto
- Explorar la distribución de películas y series en el catálogo de Netflix.

- Analizar los géneros más populares y su relación con el tipo de contenido.

- Identificar los países que producen más contenido.

- Estudiar las tendencias temporales de contenido añadido a Netflix.

- Explorar la duración de películas y series.

- Analizar la clasificación por edad del contenido.

## Herramientas Utilizadas
- Python: Lenguaje de programación principal.

- Pandas: Para manipulación y análisis de datos.

- Matplotlib y Seaborn: Para visualización de datos.

- Jupyter Notebook: Para ejecutar y documentar el análisis.

# Pasos del Análisis
## Instrucciones para Ejecutar el Proyecto
Clona este repositorio:

`bash`
```python
git clone https://github.com/GilbertoM0/Limpieza-de-datos-Netflix.git
```
## Instala las dependencias:

`bash`
```python
pip install -r requirements.txt
```

## Abre el Jupyter Notebook:
`bash`
```python
jupyter notebook notebooks/netflix_analysis.ipynb
```

## 1. Importación y Exploración Inicial
Cargar el dataset.

Explorar las primeras filas y obtener información general.

## 2. Limpieza y Preparación de Datos
Estandarizar texto (minúsculas, eliminar espacios).

Manejar valores vacios -> Desconocido.


## 3. Análisis de Datos
Distribución de películas y series.

Géneros más comunes.

Países que producen más contenido.

Tendencias temporales de contenido añadido.

Duración de películas y series.

Clasificación por edad del contenido.

## 4. Visualización de Datos
Gráficos de barras y bigotes.
Ej:

![image](https://github.com/user-attachments/assets/de895bb6-c977-4e59-a400-f46e70fac865)
