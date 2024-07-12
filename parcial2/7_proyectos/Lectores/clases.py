class Lectores:
    def __init__(self,nombre,direccion,tel):
        #Atributos
        self.nombre=nombre
        self.direccion=direccion
        self.tel=tel

    def getnombre(self):
        return self.nombre
    
    def setnombre(self,nombre):
        self.nombre=nombre

    def getdireccion(self):
        return self.direccion
    
    def setnombre(self,direccion):
        self.direccion=direccion

    def gettel(self):
        return self.tel
    
    def settel(self,tel):
        self.tel=tel

    #Metodos
    def reservar(self):
        print("Esta reservado el libro")

    def entregar(self):
        print("Esta entregado el libro")

class Estudiantes (Lectores):
    def __init__(self, nombre, direccion, tel, carrera, matricula):
        super().__init__(nombre, direccion, tel)
        #Atributos
        self._carrera=carrera
        self._matricula=matricula

    def reservar(self):
        print(f"Esta reservado el libro por el estudiante {self.getnombre()} y su matricula es {self.getmatricula()}")

    def entregar(self):
        print(f"Esta entregado el libro por el estudiante {self.getnombre()}")

    def getcarrera(self):
        return self._carrera
    
    def setcarrera(self,carrera):
        self._carrera=carrera

    def getmatricula(self):
        return self._matricula
    
    def setmatricula(self,matricula):
        self._matricula=matricula

class Docente (Lectores):
    def __init__(self, nombre, direccion, tel, modalidad, num_empleado):
        super().__init__(nombre, direccion, tel)
        #Atributos
        self.__modalidad=modalidad
        self.__num_empleado=num_empleado

    def reservar(self):
        print(f"Esta reservado el libro por el docente {self.getnombre()} y su numero de empleado es {self.getnum_empleado()}")

    def entregar(self):
        print(f"Esta entregado el libro por el docente {self.getnombre()}")

    def getmodalidad(self):
        return self.__modalidad
    
    def setmodalidad(self,modalidad):
        self.__modalidad=modalidad

    def getnum_empleado(self):
        return self.__num_empleado
    
    def setnum_empleado(self,num_empleado):
        self.__num_empleado=num_empleado