#  Práctica 1: Web scraping
##  Descripción

En esta práctica correspondiente a la  asignatura Tipología y ciclo de vida de los datos, perteneciente al Máster en Ciencia de Datos de la Universitat Oberta de Catalunya. Se  aplican técnicas correspondientes al web scraping , bajo  el lenguaje de programación Python, para extraer datos  de los paises del mundo procedentes de distintas páginas del siti web Wikipedia. Con el objetivo de generar un dataset final que los agrupe.

## Miembros del equipo

Martín Sánchez Pueyo y Marina Peña Alonso

## Ficheros del código fuente

+ **driver.py** Ejecuta el driver mediante la herramienta Selenium y cambia el agente de usuario o Usaer agent para no ser bloqueado y detectado en algunos casos por los robots.
+ **utils.py** Función encargada de limpiar las celdas escrapeadas.
+ **table.py** Script que realiza el proceso de scrapeamiento llamando y aplicando a los scripts anteriores y almacena los datos extraidos de la web en su correspondiente csv.
+ **main.py** Función encargada de pasar el url, xpath y el nombre del csv de los datos que queremos extaer de la wikipedia.
+ **csv_handler.py** Se encarga de agrupar los csv creados anteriormente en uno solo para presentarlo como resultado final.

## Comentarios

Debido a la función de limpieza de cada celda el script requiere de mucho tiempo para ser ejecutado.

## Recursos

1. Lawson, R. (2015). Web Scraping with Python. Packt Publishing Ltd. Chapter 2. Scraping the Data.
2. Mitchel, R. (2015). Web Scraping with Python: Collecting Data from the Modern Web. O'Reilly Media, Inc. Chapter 1. Your First Web Scraper.


