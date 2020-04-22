import math
class Procesos():
	'''nombre = Nombre de proceso,
	   TE = Tiempo de ejecucion,
	   MI = Momento de inicio'''
	def __init__(self, nombre, TE, MI): 
		self._nombre = nombre
		self._TE = TE
		self._MI = MI
		self._TCC = 0
		self._TVC = 0
		self._TB = 0
		self._TT = 0
		self._TI = 0
		self._TF = 0

	def calcularTB(self, bloqueos):
		if (self._TE <= 400):
			self._TB = 2 * bloqueos
		elif(self._TE <= 600): 
			self._TB = 3 * bloqueos
		elif(self._TE <= 800):
			self._TB = 4 * bloqueos
		else:
			self._TB = 5 * bloqueos
	
	def calcularTVC(self, quantum, TCC):
		if(quantum < self._TE):
			self._TVC = self._TE / quantum
			self._TVC = (math.ceil(self._TVC)-1) * TCC
			print(self._TVC)
		else:
			self._TVC = 0
			print(self._TVC)

	def calcularTF(self, TI, TT):
		self._TF = self._TI + self._TT
		print(self._TF)

	def calcularTT(self):
		self._TT = self._TCC + self._TE + self._TVC + self._TB 
		print(self._TT)

	def calculoFinal(self, T_Ini, TI_CC, quantum, TI_Bloqueo, Micro_TCC):
		self.TI = T_Ini
		self.TCC = TI_CC
		self.calcularTVC(quantum,Micro_TCC)
		self.calcularTB()
		self.calcularTT()
		self.calcularTF()

	def get_nombre(self): 
		return self._nombre
	  
	def set_nombre(self, x): 
		self._nombre = x
 
	def get_TE(self): 
		return self._TE 
	  
	def set_TE(self, x): 
		self._TE = x

	def get_MI(self): 
		return self._MI 
	  
	def set_MI(self, x): 
		self._MI = x


def main():
	nuevo_proceso = Procesos("B",300,0)
	bloqueos = int(input("bloqueos: "))
	nuevo_proceso.calcularTB(bloqueos)
	quantum = int(input("quantum: "))
	TCC = int(input("tcc: "))
	nuevo_proceso.calcularTVC(quantum,TCC)
	nuevo_proceso.calcularTT()

	
	
	


if __name__ == '__main__':
	main()




