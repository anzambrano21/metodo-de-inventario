""" 
Q cantidad de inventario. 
D es tasa de la demanda. 
R tasa de produccion 
"""
from math import sqrt
class Lepp:
# Constructor de la clase del modelo lepp e inicializando las variables 
# de tasa de produccion (Tp) y tasa de demanda (td) 
#
    def __init__(self):
        self.Tp=0
        self.td=0
        self.c
    def costo(self,costoP,costoOp,costoMi):
        q=self.cantidadInv(costoOp,costoMi)
        self.c=costoP*q+costoOp+costoMi*(pow(q,2)*(1-self.td/self.Tp))/self.td*2
        return self.c
    #tasa de produccion
    def setTp(self,Tp):
        self.Tp=Tp
    #tasa de demanda
    def setTp(self,td):
        self.td=td
    def cantidadInv(self,costoOp,costoMi):
        return sqrt((2*self.td*costoOp)/(costoMi*(1-self.td/self.Tp)))
class LeppFal(Lepp):
    def __init__(self):
        super().__init__()
    def costo(self,costoP,costoOp,costoMi,cf):
        q=super().cantidadInv(costoOp,costoMi)*sqrt((costoMi+cf)/cf)
        s=sqrt(2*self.td*costoOp/cf)*sqrt(1-self.td/self.Tp)*sqrt(costoMi/(costoMi+cf))
        self.c=costoP*q+costoOp+(costoMi/2)*pow(q*(1-self.td/self.Tp)-s,2)*(1/(self.Tp-self.Tp)+1/self.td)+(cf*s*s/2)*(1/(self.Tp-self.Tp)+1/self.td)
        return self.c


