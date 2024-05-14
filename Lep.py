""" Q cantidad de inventario D  es tasa de la demanda R tasa de produccioon """
from math import sqrt
class Lepp:
    
    def __init__(self):
        self.Tp=0
        self.td=0
        self.c
    def costo(self,costoP,costoOp,costoMi):
        q=sqrt((2*self.td*costoOp)/(costoMi*(1-self.td/self.Tp)))
        self.c=costoP*q+costoOp+costoMi*(pow(q,2)*(1-self.td/self.Tp))/self.td*2
    #tasa de produccion
    def setTp(self,Tp):
        self.Tp=Tp
    #tasa de demanda
    def setTp(self,td):
        self.td=td

