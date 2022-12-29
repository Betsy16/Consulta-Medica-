
from pacientes import paciente, personal
import os

class diagnostico():
    def __init__(self,diagnostico, horario, sintomas, tratamientos):
        self.diagnostico = diagnostico
        self.horario = horario
        self.sintomas = sintomas
        self.tratamiento = tratamientos
        
    def mostrardiagnostico(self):
        print(f"*"*15, "Diagnostico Medico", "*"*15)
        print(f"Horario:",self.horario)
        print(f"Sintomas:",self.sintomas)
        print(f"Diagnostico Medico:",self.diagnostico)
        print(f"Tratamiento:",self.tratamiento)
        
if __name__ == '__main__':
    
    os.system("cls")
    med = personal("Ruben","0999999999","ruben@gmail.com","0999999999")
    pac = paciente("Betsy","0999999999","betsy@gmail.com","0999999999","Femenino","22")
    diag = diagnostico("Falta de hierro","14:00 PM","Fiebre, Mareo, Vomitos","Tomar cada 12 hrs 2 umbral 500mg")
    med.mostrarusuarios()
    pac.mostrarusuarios()
    diag.mostrardiagnostico()
    