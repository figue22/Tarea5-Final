from datetime import date
from models.gasto import Gasto
from models.tipoPago import tipoPago


class Viaje:

    def __init__(self, lugarDestino: str, fechaInicio: date, fechaFinal: date, presupuestoPorDia: float):
        self.__lugarDestino = lugarDestino
        self.__fechaInicio = fechaInicio
        self.__fechaFinal = fechaFinal
        self.__presupuestoPorDia = presupuestoPorDia
        self.__gastos = []



    def getLugarDestino(self):
      return self.__lugarDestino
    
    def getFechaInicio(self):
        return self.__fechaInicio
    
    def getFechaFinal(self):
        return self.__fechaFinal
    
    def getPresupuestoPorDia(self):
        return self.__presupuestoPorDia
    
    def getGastos(self):
        return self.__gastos
    

    def agregarGasto(self, fecha, valorGastado, metodoPago, tipoGasto):
        if fecha < self.__fechaInicio or fecha > self.__fechaFinal:
            raise ValueError("La fecha del gasto no corresponde al rango del viaje")
        
        else:
            gasto = Gasto(fecha, valorGastado, metodoPago, tipoGasto)
            gasto.convertiCop(self.__lugarDestino)
            self.__gastos.append(gasto)
            gastoTotal = 0

            for gasto in self.__gastos:
                if fecha == gasto.getFecha():
                    gastoTotal += gasto.getValorGastado()

            diferencia = self.__presupuestoPorDia- gastoTotal

            print("="*40)
            print(f"{' GASTO ':^40}")
            print("="*40)
            print(f"Fecha: {fecha}")
            print(f"Valor: {gasto.getValorGastado():,} COP")
            print(f"Metodo de pago: {metodoPago.name}")
            print(f"Tipo de gasto: {tipoGasto.name}")
            print("-"*40)
            print(f"Presupuesto diario: {self.__presupuestoPorDia:,} COP")
            print(f"Total gastado a la fecha: {gastoTotal:,} COP")
            print(f"Diferencia con el presupuesto diario: {diferencia:,} COP")
            print("="*40)
            print("\n")


    def obtenerReporte(self):
        reporte = {}
        total_general = 0

        for gasto in self.__gastos:
            fecha = gasto.getFecha()
            valor = gasto.getValorGastado()
            metodo = "efectivo" if gasto.getTipoPago() == tipoPago.EFECTIVO else "tarjeta"

            if fecha not in reporte:
                reporte[fecha] = {"efectivo": 0, "tarjeta": 0, "total": 0}

            reporte[fecha][metodo] += valor
            reporte[fecha]["total"] += valor
            total_general += valor

        print("="*40)
        print(f"{' REPORTE FINAL DEL VIAJE ':^40}")
        print("="*40)

        for fecha, valores in sorted(reporte.items()):
            print(f"Fecha: {fecha}")
            print(f"Gasto en efectivo: {valores['efectivo']:,} COP")
            print(f"Gasto con tarjeta: {valores['tarjeta']:,} COP")
            print(f"Total gastado: {valores['total']:,} COP")
            print("-"*40)

        print(f"Total general gastado en el viaje: {total_general:,} COP")
        print("="*40)
        print("\n")

        return reporte





