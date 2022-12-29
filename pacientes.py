from abc import ABC,abstractmethod 
import os

class usuarios(ABC):
    def __init__(self, nom, ced, mail, tel):
        self.nombre = nom
        self.cedula = ced
        self.correo = mail
        self.telefono = tel
    
    @abstractmethod
    def mostrarusuarios(self):
        pass
    
class personal(usuarios):
    def __init__(self, nom, ced, email, tel):
        super().__init__(nom, ced, email, tel)
        
        
    def mostrarusuarios(self):
        print(f"*"*15, "Personal", "*"*15)  
        print(f"Medico:",self.nombre, "", "Cedula:",self.cedula)
        

class paciente(usuarios):
    def __init__(self, nom, ced, email, tel, genero, edad):
        super().__init__(nom, ced, email, tel)
        self.genero = genero
        self.edad = edad
        
    def mostrarusuarios(self):
        print(f"*"*15, "Pacientes", "*"*15)
        print(f"Paciente:",self.nombre, "", "Cedula:",self.cedula)
        
if __name__ == '__main__':
    
    
    os.system("cls")      
    med = personal("Ruben","099999999","ruben@gmail.com","099999999")
    med.mostrarusuarios()
    pac = paciente("Betsy","099999999","betsy@gmail.com","099999999","Femenino","22")
    pac.mostrarusuarios()