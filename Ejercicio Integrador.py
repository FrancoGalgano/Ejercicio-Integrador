#################################
#   Resolución del ejercicio 7  #
#################################

###     Defino clase Cuenta     ###

class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

###     Defino los getters y los setters    ###
    def getter_titular(self):
        return self.titular
    
    def getter_cantidad(self):
        return self.cantidad
    
    def deposito(self, deposito):
        if deposito > 0:
            self.cantidad += float(deposito)

    def retiro(self, retiro):
        if retiro > 0:
            self.cantidad -= float(retiro)

###     Defino mostrar    ###    
    def mostrar(self):
        return print(f"Titular de la cuenta: {self.titular} \nCantidad de la cuenta: {self.cantidad}")

#################################
#   Resolución del ejercicio 8  #
#################################

####      Defino Cuenta Joven a partir de clase Cuenta       #####

class CuentaJoven (Cuenta):
    def __init__(self, titular, edad, cantidad=0.0, porcentaje=0):
        super().__init__(titular, cantidad)
        self.edad = int(edad)
        self.porcentaje = int(porcentaje)

####      Defino método es_titular_() como es un booleano       #####

    def es_titular_valido(self):
        return self.edad >= 18 and self.edad < 25

####      Defino los getters y los setters para Cuenta Joven       #####

    def getter_porcentaje(self):
        return self.porcentaje
    
    def setter_porcentaje(self, porcentaje):
        self.porcentaje = porcentaje
    

    def deposito(self, deposito):
        if deposito > 0:
            self.cantidad += float(deposito)

    def retiro(self, retiro):
        if self.es_titular_valido():
            self.cantidad -= float(retiro)

####      Defino mostrar para Cuenta Joven       #####

    def mostrar(self):
        if self.es_titular_valido():
            return print(f"Cuenta Joven\nEs titular valido\nSu porcenaje de descuento es: {self.porcentaje}%")
        else:
            return print(f"Titular de la cuenta: {self.titular} \nNO es titular valido")

