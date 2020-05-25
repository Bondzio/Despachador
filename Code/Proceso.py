import math

class Proceso:
    def __init__(self, nombre, TE, MI):
        self._nombre = nombre
        self._MI = MI
        self._TE = TE
        self.TB = 0 
        self.TCC = 0 
        self.TVC = 0 
        self.TT = 0 
        self.TI = 0 
        self.TF = 0 

    def calcular_TVC(self, quantum, TCC):
        self.TVC = (math.ceil(self._TE / quantum) -1) * TCC

    def calcular_TB(self, bloqueos):
        if (self._TE <= 400):
            self.TB = 2 * bloqueos
        elif(self._TE <= 600): 
            self.TB = 3 * bloqueos
        elif(self._TE <= 800):
            self.TB = 4 * bloqueos
        else:
            self.TB = 5 * bloqueos

    def calcular_TT(self):
        self.TT = self.TCC + self._TE + self.TVC + self.TB

    def get_nombre(self):
        return self._nombre

    def get_MI(self):
        return self._MI

    def get_TT(self):
        return self.TT

    def set_TI(self, x): 
        self.TI = x

    def set_TCC(self, x): 
        self.TCC = x


    def __repr__(self):
        return "\n<Nombre:%s TCC:%s TE:%s TVC:%s TB:%s TT:%s TI:%s TF:%s>" % (self._nombre, self.TCC, self._TE, self.TVC, self.TB, self.TT, self.TI, self.TF)

    def __str__(self):
        return "From str method of Procesos: nombre es %s, TCC es %s, TE es %s, TVC es %s, TB es %s, TT es %s, TI es %s, TF es %s," %  (self._nombre, self.TCC, self._TE, self.TVC, self.TB, self.TT, self.TI, self.TF)



