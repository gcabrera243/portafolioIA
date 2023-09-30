Title: PD1 - Procesamiento previo de los datos - Wine
Date: 2023-09-03 10:20
Category: UT2
cover:
tags: ['PDs'] 

En este artículo, seguiremos los tutoriales de RapidMiner "Handling Missing Values" y "Normalization and Outlier detection" para la preparacion de datos y luego utilizaremos el conjunto de datos Wine de la UCI como ejemplo práctico para demostrar lo aprendido.

## Aprendizaje de RapidMiner
En RapidMiner Studio, ve a la sección de Help / Tutorials, y de la parte “Prepare Data” completa
los tutoriales:
1. ”Handling Missing Values” y
2. ”Normalization and Outlier detection”

Gracias a los tutoriales de RapidMiner, hemos adquirido un profundo conocimiento de las herramientas disponibles para el procesamiento de datos, selección de características y diversas técnicas de normalización.
Durante el análisis de los datos, hemos reconocido la importancia de la normalización. Además, hemos identificado valores atípicos en ciertas instancias y notado la presencia de valores faltantes en algunos atributos.

<!-- Faltan los dos .rmp -->

## Ejemplo Práctico
Problema planteado: Determinar la clase de vino a partir de sus concentraciones de varios nutrientes. Se trata de un problema de clasificacion donde vamos a tener 3 clases.


Variable objetivo: class (clase de vino) que es de tipo categórico
<!-- Falta imagen de los atributos y sus tipos -->

Los atributos Magnesium y Proline son de tipo numérico entero.
La mayoría de atributos son de tipo numérico de punto flotante.

Atributo					Tipo	
class						Categorical
Alcohol						Continuous
Malicacid					Continuous
Ash						Continuous
Alcalinity_of_ash				Continuous
Magnesium					Integer
Total_phenols					Continuous
Flavanoids					Continuous
Nonflavanoid_phenols				Continuous
Proanthocyanins					Continuous
Color_intensity					Continuous
Hue						Continuous
0D280_0D315_of_diluted_wines			Continuous
Proline						Integer

Se detectaron 10 outliers en los datos.
<!-- Imagen Outliers -->


Se crearon dos canales, uno donde se utiliza el dataset tal cual esta y otro en donde se aplican bloques para normalizar y estandarizar los datos.

para el dataset sin bloques:
![performance1](https://github.com/gcabrera243/portafolioIA/tree/main/content/UT2/PDs/PD1/PerformanceSinNormalizar.png?raw=true)

Para el dataset con bloques:
<!-- Imagen Performance Normalizado -->

Dio mejor la performance de los datos sin normalizar en este caso. Esto puede ser por el split actual de datos.
<!-- Falta el .rmp -->

