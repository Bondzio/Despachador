Despachador
===================================
Proyecto para la clase de Sistemas Operativos en donde se tuvo que desarrollar un despachador simple para el cálculo de procesos en N microprocesadores. Esta hecho en python y falta interfaz gráfica. Los procesos deben aparecer ordenados por el momento en que terminaron y deben incluirse los huecos.
## Los datos de entrada son los siguientes:
* Número de microprocesadores
* Quantum
* Tiempo para cambio de contexto
* Tiempo para bloqueo

## Proceso.py
Se definieron todas las características de un proceso con sus métodos. El cálculo de tiempo para cambio de contexto (TCC), tiempo de bloqueo (TB) y tiempo total (TT) se definieron en esta clase.

## Micro.py
En la clase Micro se define un arreglo de procesos que ingresan en el micro. Desde el arreglo se agregan al micro, se define un método de agregar huecos, calcular el tiempo de vencimiento de quantum (TVC) y la suma del tiempo total (TT).

## Despachador.py
En esta clase se define un arreglo de micros que va a decidir a donde va cada proceso que se encuentre en la lista de procesos. Para la decisión primero se toma en cuenta el id del micro y después por su tiempo total.

## test.py
Este es el archivo que se debe de correr para probar el despachador. La lista de procesos se define de la siguiente manera:
* Donde la primera instancia de Proceso es el nombre, luego su tiempo de ejecución (TE) y por último el momento de inicio del proceso (MI). 

		Proceso("B", 300,  0),
		Proceso("D", 100,  0),
		Proceso("F", 500,  0),
		Proceso("H", 700,  0),
		Proceso("J", 300,  1500),
		Proceso("L", 3000, 1500),
		Proceso("N", 50,   1500),
		Proceso("O", 600,  1500),
		Proceso("A", 400,  3000),
		Proceso("C", 50,   3000),
		Proceso("E", 1000, 3000),
		Proceso("G", 10,   3000),
		Proceso("I", 450,  3000),
		Proceso("K", 100,  4000),
		Proceso("M", 80,   4000),
		Proceso("P", 800,  4000),
		Proceso("Ñ", 500,  8000)]
