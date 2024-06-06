
from datetime import date

import requests

from models import tipoGasto, tipoPago


class Gasto:

    def __init__(self, fecha: date, valorGastado: float, tipoPago: tipoPago, tipoGasto: tipoGasto):
        self.__fecha = fecha
        self.__valorGastado = valorGastado
        self.__tipoPago = tipoPago
        self.__tipoGasto = tipoGasto


    def getValorGastado(self):
        return self.__valorGastado

    def getFecha(self):
        return self.__fecha
    
    def getTipoPago(self):
        return self.__tipoPago
    
    def getTipoGasto(self):
        return self.__tipoGasto
    
    def setValorGastado(self, valorGastado):
        self.__valorGastado = valorGastado

    def setFecha(self, fecha):
        self.__fecha = fecha

    def setTipoPago(self, tipoPago):
        self.__tipoPago = tipoPago

    def setTipoGasto(self, tipoGasto):
        self.__tipoGasto = tipoGasto


    def convertiCop(self, lugarDestino):
        if lugarDestino == 'Estados Unidos':
            print("Se convierte el valor de dolares a pesos")
            valorRandom = self.uso_api()
            self.__valorGastado = self.__valorGastado * valorRandom

        if lugarDestino == 'Europa':
            print("Se convierte el valor de euros a pesos")
            valorRandom = self.uso_api()
            self.__valorGastado = self.__valorGastado * (valorRandom + 200)



    def uso_api(self):
        response = requests.get("https://csrng.net/csrng/csrng.php?min=3500&max=4500")
        random = response.json()[0]["random"]
        return random


 