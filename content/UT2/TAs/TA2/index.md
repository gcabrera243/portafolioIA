Title: TA2 - Procesamiento previo de los datos - Wine
Date: 2023-09-03 10:20
Category: UT2
cover:
tags: ['TAs'] 

En este artículo, utilizaremos el conjunto de datos Wine de la UCI como ejemplo práctico para demostrar lo aprendido de normalizacion.

## Problema
Problema planteado: Determinar la clase de vino a partir de sus concentraciones de varios nutrientes. Se trata de un problema de clasificacion donde vamos a tener 3 clases.


Variable objetivo: class (clase de vino) que es de tipo categórico
<!-- Falta imagen de los atributos y sus tipos -->

## Atributos
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

## Canales
Se crearon dos canales, uno donde se utiliza el dataset tal cual esta y otro en donde se aplican bloques para normalizar y estandarizar los datos.

para el dataset sin bloques:
<!-- Imagen Performance sin Normalizar -->

Para el dataset con bloques:
<!-- Imagen Performance Normalizado -->

Dio mejor la performance de los datos sin normalizar en este caso. Esto puede ser por el split actual de datos.
<!-- Falta el .rmp -->

