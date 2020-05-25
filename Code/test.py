from Despachador import *
from Proceso import *

def main():
	proceso = [
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

	quantum = int(input("Quantum: "))
	while quantum <= 0:
		print ("¡No hay números negativos!")
		quantum = int(input("Quantum: "))
	tb = int(input("TB: "))
	while tb < 0:
		print ("¡No hay números negativos!")
		tb = int(input("TB: "))
	tcc = int(input("TCC: "))
	while tcc < 0:
		print ("¡No hay números negativos!")
		tcc = int(input("TCC: "))
	microsN = int(input("Número de micros: "))
	while microsN == 0 or microsN < 0 or microsN > 100:
		print ("¡Recuerda que no puede haber números negativos, 0 micros o más de 100 micros!")
		microsN = int(input("Micros: "))

	print()
	print()
	despachador = Despachador(quantum, tb, tcc, microsN, proceso)
	despachador.imprimir_Tablas()
			
if __name__ == '__main__':
	main()
