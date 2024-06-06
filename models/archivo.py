from models.viaje import Viaje
from models.tipoPago import tipoPago


class Archivo:

    def __init__(self, nombreArchivo, viaje: Viaje):
        self.__nombreArchivo = nombreArchivo
        self.__viaje = viaje
       


    
    def generarArchivo(self):
        viaje = self.__viaje
        with open(self.__nombreArchivo, 'w', encoding='utf-8') as file:
            file.write("="*40 + "\n")
            file.write(f"{' INFORMACIÓN DEL VIAJE ':^40}\n")
            file.write("="*40 + "\n")
            file.write(f"Lugar de destino: {viaje.getLugarDestino()}\n")
            file.write(f"Fecha de inicio: {viaje.getFechaInicio()}\n")
            file.write(f"Fecha final: {viaje.getFechaFinal()}\n")
            file.write(f"Presupuesto por día: {viaje.getPresupuestoPorDia():,} COP\n")
            file.write("="*40 + "\n")

            gastos = viaje.getGastos()
            if gastos:
                file.write(f"{' GASTOS ':^40}\n")
                file.write("="*40 + "\n")

                for gasto in gastos:
                    file.write(f"Fecha: {gasto.getFecha()}\n")
                    file.write(f"Valor: {gasto.getValorGastado():,} COP\n")
                    file.write(f"Metodo de pago: {'efectivo' if gasto.getTipoPago() == tipoPago.EFECTIVO else 'tarjeta'}\n")
                    file.write(f"Tipo de gasto: {gasto.getTipoGasto().name}\n")
                    file.write("-"*40 + "\n")

                reporte = {}
                total_general = 0

                for gasto in gastos:
                    fecha = gasto.getFecha()
                    valor = gasto.getValorGastado()
                    metodo = "efectivo" if gasto.getTipoPago() == tipoPago.EFECTIVO else "tarjeta"

                    if fecha not in reporte:
                        reporte[fecha] = {"efectivo": 0, "tarjeta": 0, "total": 0}

                    reporte[fecha][metodo] += valor
                    reporte[fecha]["total"] += valor
                    total_general += valor

                file.write(f"{' REPORTE FINAL DEL VIAJE ':^40}\n")
                file.write("="*40 + "\n")

                for fecha, valores in sorted(reporte.items()):
                    file.write(f"Fecha: {fecha}\n")
                    file.write(f"Gasto en efectivo: {valores['efectivo']:,} COP\n")
                    file.write(f"Gasto con tarjeta: {valores['tarjeta']:,} COP\n")
                    file.write(f"Total gastado: {valores['total']:,} COP\n")
                    file.write("-"*40 + "\n")

                file.write(f"Total general gastado en el viaje: {total_general:,} COP\n")
                file.write("="*40 + "\n")
            else:
                file.write("No hay gastos registrados para este viaje.\n")
                
        return file