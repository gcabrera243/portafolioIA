Title: TA1 - Procesamiento previo de los datos - Wine
Date: 2023-09-03 10:20
Category: UT2
cover:
tags: ['TAs'] 

En este articulo, investigaremos el dataset de titanic.

# Problema 

Se busca predecir dado los datos que se conocen antes de embarcar, si la persona embarcada sobrevivirá o no.

# Atributos
<!-- Falta imagen de atributos -->

De estas estadísticas se puede ver que faltan:
<!-- Cambiar texto -->
- 263 edades
- 1 passangare fare
- 1014 cabinas
- 2 puertos de embarcación
- 823 botes salvavidas

# Tratamiento de los datos

Los errores encontrados fueron:
- Incluir botes salvavidas o numero de cuerpo, esto no tiene sentido ya que al momento de embarcación no es posible saber esta información
- Es necesario reemplazar los valores faltantes, en este caso se utilizó el promedio de los mismos
- Se normalizaron los datos

# Correlaciones

Analizando la matriz de correlación y sus pesos podemos ver:


<!-- Imagenes -->

Un factor importante a tener en cuenta es la edad del pasajero, y siguiente es el passanger fare, también lo será el passanger class.

<!-- Poner rmp-->