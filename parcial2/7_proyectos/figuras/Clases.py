import math

class Figura:
        def CalcularArea(self):
            pass

class Rectangulo(Figura):
        def __init__(self,largo,ancho):
            self._largo=largo
            self._ancho=ancho

        def getLargo(self):
            return self._largo

        def setLargo(self,largo):
            self._largo=largo       

        def getAncho(self):
            return self._ancho

        def setLargo(self,ancho):
            self._ancho=ancho 

        def CalcularArea(self):
            Resultado=self.getLargo()*self.getAncho()
            return Resultado

class Circulo(Figura):
        def __init__(self,radio):
            self._radio=radio

        def getRadio(self):
            return self._radio

        def setRadio(self,radio):
            self._radio=radio
            

        def CalcularArea(self):
            Resultado=(self.getRadio()**2)*math.pi
            return Resultado

class Triangulo(Figura):
        def __init__(self,altura,ancho):
            self._altura=altura
            self._ancho=ancho

        def getAltura(self):
            return self._altura

        def setAltura(self,altura):
            self._altura=altura

        def getAncho(self):
            return self._ancho

        def setAncho(self,ancho):
            self._ancho=ancho

        def CalcularArea(self):
            Resultado=(self.getAncho()*self.getAltura())/2
            return Resultado