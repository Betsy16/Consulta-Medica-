import os

class historiaclinica:
    ID = 0
    def __init__(self, nom,apepaterno,apematerno,ced,fechanacimiento,edad,antecedentes,email,tel):
        historiaclinica.ID += 0
        self.nom = nom
        self.apellidopaterno = apepaterno
        self.apellidomaterno = apematerno
        self.cedula = ced
        self.fnacimiento = fechanacimiento
        self.edad = edad
        self.correo = email
        self.telefono = tel
        self.antecedentes = antecedentes
        
    @property
    def id(self):
        return self.ID
    
    def mostrarhistclinica(self):
        print(f"ID: ",self.id)
        print(f"Nombre: ",self.nom)
        print(f"Apellido Paterno: ",self.apellidopaterno)
        print(f"Apellido Materno: ",self.apellidomaterno)
        print(f"Cedula: ",self.cedula)
        print(f"Fecha Nacimiento: ",self.fnacimiento)
        print(f"Edad: ",self.edad)
        print(f"Correo: ",self.correo)
        print(f"Telefono: ",self.telefono)
        print(f"Antecedentes: ",self.antecedentes)
        
os.system("cls")
print(f"*"*15, "Historia Clinica", "*"*15)
pac = historiaclinica("Betsy","Catuto","Cuenca","09999999","15/11/2001","22","Alergias, Varicela","betsy@gmail.com","099999999")
pac.mostrarhistclinica()
print(f"*"*15, "Historial Clinico", "*"*15)
