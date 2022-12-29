from datetime import date
from titulo import titulo
from pacientes import paciente
from cita import diagnostico
import os

class Articulo:
    secuencia=0
    def __init__(self,des,pre,sto):
        Articulo.secuencia += 1
        self.descripcion = des
        self.precio = pre   
        self.stock = sto
    
    @property
    def id(self):
        return self.secuencia
        
    def mostrarArticulo(self):
        print(self.codigo,self.descripcion)

class detallereceta:
    _linea=0
    def __init__(self,articulo,cantidad):
        detallereceta._linea += 1
        self.linea = detallereceta._linea
        self.articulo = articulo
        self.precio = articulo.precio
        self.cantidad = cantidad


class receta:
    _factura = 0
    iva = 0.12
    def __init__(self,paciente,diagnostico):
        receta._factura += 1
        self.factura = "F"+str(receta._factura)
        self.fecha = date.today()
        self.paciente = paciente
        self.diagnostico = diagnostico
        self.subtotal = 0
        self.iva = 0
        self.total = 0
        self.detallemedicamentos = []
        
        
    def agregardetalle(self,articulo,cantidad):
        detalle = detallereceta(articulo,cantidad)
        self.subtotal += round(detalle.precio*detalle.cantidad,2)
        self.iva = round(self.subtotal*receta.iva,2)
        self.total = round(self.subtotal+self.iva,2)
        self.detallemedicamentos.append(detalle)    
    
    def mostrarreceta(self,orgnom,orgruc):
        print("Empresa: {:12} Ruc:{}".format(orgnom,orgruc)) 
        print("Factura#:{:13} Fecha:{}".format(self.factura,self.fecha))
        self.paciente.mostrarusuarios()
        self.diagnostico.mostrardiagnostico()
        print("*"*50)
        print("Linea Articulo     Precio Cantidad Subtotal")
        for det in self.detallemedicamentos:
            print("{:5} {:15} {} {:6} {:7}".format(det.linea,det.articulo.descripcion,det.precio,det.cantidad,det.precio*det.cantidad))
        print("")  
        print("="*10,"Subtotal=> ",self.subtotal)
        print("="*10,"Iva=> ",self.iva)
        print("="*10,"Total=> ",self.total) 
        
os.system("cls")     
org = titulo()    
pac = paciente("Betsy","09999999","betsy@gmai.com","099999999","Femenino","22")
med = diagnostico("Falta de hierro","14:00 PM","Dolor de cabeza, Dolor de huesos, Mareo, Vomitos","Tomar cada 12hrs 2 umbral")      
art1 = Articulo("Paracetamol",3,200)
rec = receta(pac,med)
rec.agregardetalle(art1,3)
rec.mostrarreceta(org.nombre, org.ruc)