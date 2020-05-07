from Proceso import *

class Micro:
    def __init__(self, microID, TCC, quantum, TB):
        self._id = microID
        self._TCC = TCC
        self._quantum = quantum
        self._TB = TB
        self.TT = 0
        self.proceso = [] 
        self.isTaken = False 

    def agregar_Proceso(self, proceso):
        proceso_TCC = 0
        if (self.isTaken):
            proceso_TCC = self._TCC
        proceso.set_TI(self.TT)
        proceso.set_TCC(proceso_TCC)
        proceso.calcular_TVC(self._quantum, self._TCC)
        proceso.calcular_TB(self._TB)
        proceso.calcular_TT()
        proceso.TF = proceso.TI + proceso.TT
        self.proceso.append(proceso)
        self.TT += proceso.get_TT()
        self.isTaken = True
        if (self.TT < proceso.get_MI()):
            tiempo_espera = proceso.get_MI() - self.TT
            self.proceso_Hueco(tiempo_espera)

    def proceso_Hueco(self, tiempo):
        proceso_espera = Proceso("Hueco", tiempo, 0)
        proceso_espera.set_TI(self.TT)
        proceso_espera.set_TCC(0)
        proceso_espera.calcular_TVC(tiempo, 0)
        proceso_espera.calcular_TB(0)
        proceso_espera.calcular_TT()
        proceso_espera.TF = proceso_espera.TI + proceso_espera.TT
        self.proceso.append(proceso_espera)
        self.TT += tiempo
        self.isTaken = False

    def checar_TCC(self):
        wait = 0
        for p in reversed(self.proceso):
            if(p.get_nombre() == "Hueco"):
                wait += 1
            else:
                break
        for i in range(0, wait):
            self.proceso.pop()

    def get_id(self):
        return self._id

    def get_TT(self):
        return self.TT

    def __repr__(self):
        return "\n<Micro:%s Quantum:%s TCC:%s TB:%s TT:%s \nProceso:%s \nOcupado:%s>" % (self._id, self._quantum, self._TCC, self._TB, self.TT, self.proceso, self.isTaken)

    def __str__(self):
        return "From str method of Micros: Micro es %s, Quantum es %s, TCC es %s, TB es %s, TT es %s, Proceso es %s, Taken es %s," % (self._id, self._quantum, self._TCC, self._TB, self.TT, self.proceso, self.isTaken)


