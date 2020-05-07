from operator import itemgetter
from Micro import *

class Despachador:
    def __init__(self, quantum, TB, TCC, numMicros, lista_proceso):
        self._quantum = quantum
        self._TB = TB
        self._TCC = TCC
        self.micro = []

        for i in range(0, numMicros):
            self.micro.append({"id" : i + 1,"TT" : 0,"Micro" : Micro(i + 1, self._TCC, self._quantum, self._TB)})
        self.proceso = lista_proceso
        self.agregar_Proceso()
        self.checar_TCC()

    def imprimir_Tablas(self):
        i = 1
        for m in self.micro:
            if(m["id"] == i):
                print(m.values())
            i += 1
    
    def agregar_Proceso(self):
        for p in self.proceso:
            micro_actual = self.seleccionar_micro()
            if micro_actual["Micro"].get_TT() < p.get_MI():
                for m in self.micro:
                    if m["Micro"].get_TT() < p.get_MI():
                        tiempo_espera = p.get_MI() - m["Micro"].get_TT()
                        m["Micro"].proceso_Hueco(tiempo_espera)
                        m["TT"] = m["Micro"].get_TT()
                micro_actual = self.seleccionar_micro()
            micro_actual["Micro"].agregar_Proceso(p)
            micro_actual["TT"] = micro_actual["Micro"].get_TT()

    def checar_TCC(self):
        for m in self.micro:
            m["Micro"].checar_TCC()

    def seleccionar_micro(self):
        micro_ordenado = sorted(self.micro, key=itemgetter('id'))
        micro_ordenado = sorted(micro_ordenado, key=itemgetter('TT'))
        return micro_ordenado[0]
        
    def __repr__(self):
        return "<Quantum:%s TB:%s TCC:%s Micros:%s>" % (self._quantum, self._TB, self._TCC, self.micro)

    def __str__(self):
        return "Quantum:%s, TB:%s, TCC:%s, Micros:%s," % (self._quantum, self._TB, self._TCC, self.micro)

