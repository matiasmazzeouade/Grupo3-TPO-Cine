
Grupo3-TPO-Cine 

Informe del Trabajo Práctico Final – Programación 1

Sistema de Gestión de Cine

Grupo 3: Matías Mazzeo, Facundo López, Marcos Grupillo, Santiago Zunich y Juan Ferrandini
Profesores: Nardone Juan Pablo y Guzman Gustavo Damian

Introducción

El trabajo consistió en armar un sistema de gestión para un cine. Con este programa se pueden manejar películas, clientes, salas, funciones y reservas. Además, agregamos la posibilidad de consultar estadísticas en base a la información cargada.

El desarrollo fue paso a paso: empezamos con matrices, y de a poco lo fuimos mejorando hasta llegar a un sistema modular, con listas y diccionarios. También fuimos sumando lo que veíamos en clase: validaciones, expresiones regulares, uso de tuplas y conjuntos, etc.

Estructura del Sistema

El sistema se organizó en distintos módulos, cada uno con una responsabilidad:
•	peliculasCrud.py: gestión de películas.
•	clientesCrud.py: gestión de clientes.
•	funcionesCrud.py: manejo de funciones (película + sala + horario).
•	salasCrud.py: gestión de salas.
•	reservasCrud.py: gestión de reservas de asientos.
•	estadisticas.py: reportes y cálculos estadísticos.
•	funciones.py: utilidades de impresión y formateo.
•	base.py: menú principal e inicio del programa con datos precargados.

Funcionalidades

•	CRUD completo para películas, clientes, funciones, salas y reservas.
•	Consultas por ID, nombre o fecha (según corresponda).
•	Estadísticas como:
o	duración mínima, máxima y promedio de películas,
o	películas más reservadas,
o	análisis de edades de los clientes,
o	listado de géneros de películas y tipos de salas.
•	Validaciones de datos de entrada (por ejemplo horarios y fechas en funciones, mails y teléfonos de clientes).

Proceso de Desarrollo

El recorrido fue así:
1.	Arrancamos con las matrices: de entrada la información se guardaba en matrices, como primera práctica para ordenar datos.
2.	CRUDs básicos: después armamos las operaciones para cargar, consultar, modificar y borrar, pero ya pasando a listas de diccionarios porque era más cómodo y claro.
3.	Estadísticas: con las estructuras listas, sumamos funciones para calcular datos y hacer reportes.
4.	Mejoras al código luego de revisiones:
o	sacamos break que cortaban de más, y lo reemplazamos con banderas de control,
o	usamos diccionarios para manejar datos con claves,
o	metimos regex para validar emails y teléfonos,
o	usamos tuplas para devolver info puntual de películas,
o	y sets para quedarnos con categorías únicas (géneros, tipos de sala).

Problemas y Soluciones

En el camino tuvimos algunos problemas que fuimos resolviendo:
•	El uso de break cortaba mal algunos bucles → lo arreglamos con banderas.
•	No teníamos validación de datos como emails o teléfonos → lo resolvimos con expresiones regulares.
•	Al manejar funciones en las salas hubo que calcular bien la superposición de horarios para que no se pisen.

Conclusión

El sistema final cumple con lo que pedía la consigna:
•	CRUDs completos,
•	consultas y estadísticas,
•	uso de distintas estructuras (matrices, listas, diccionarios, tuplas, sets),
•	validaciones y expresiones regulares,
•	y un proceso de mejora continua, ya que arrancamos simple y lo fuimos puliendo clase a clase.

