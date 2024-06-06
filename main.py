import time
from models.archivo import Archivo
from models.viaje import Viaje
from models.gasto import Gasto
from models.tipoGasto import tipoGasto
from models.tipoPago import tipoPago

"""viaje = Viaje('Estados Unidos', '2021-10-10', '2021-10-20', 1000000)


viaje.agregarGasto('2021-10-10', 100, tipoPago.EFECTIVO, tipoGasto.COMPRAS)
time.sleep(3)
viaje.agregarGasto('2021-10-10', 300, tipoPago.EFECTIVO, tipoGasto.ALIMENTACION)
time.sleep(3)
viaje.agregarGasto('2021-10-10', 10, tipoPago.EFECTIVO, tipoGasto.ALOJAMIENTO)
time.sleep(3)
viaje.agregarGasto('2021-10-11', 10, tipoPago.EFECTIVO, tipoGasto.ALOJAMIENTO)
time.sleep(3)
viaje.agregarGasto('2021-10-11', 10, tipoPago.TARJETA, tipoGasto.ALOJAMIENTO)
time.sleep(3)

viaje.obtenerReporte()

archivo = Archivo(f'viaje {viaje.getLugarDestino(), viaje.getFechaInicio()}.txt', viaje)
archivo.generarArchivo()"""


viaje2 = Viaje('Europa', '2021-10-10', '2021-10-20', 1000000)
viaje2.agregarGasto('2021-10-10', 100, tipoPago.EFECTIVO, tipoGasto.COMPRAS)
time.sleep(3)
viaje2.agregarGasto('2021-10-10', 300, tipoPago.EFECTIVO, tipoGasto.ALIMENTACION)
time.sleep(3)
viaje2.agregarGasto('2021-10-10', 10, tipoPago.EFECTIVO, tipoGasto.ALOJAMIENTO)
time.sleep(3)
viaje2.agregarGasto('2021-10-11', 10, tipoPago.EFECTIVO, tipoGasto.ALOJAMIENTO)
time.sleep(3)
viaje2.agregarGasto('2021-10-11', 10, tipoPago.TARJETA, tipoGasto.ALOJAMIENTO)
time.sleep(3)

viaje2.obtenerReporte()

archivo2 = Archivo(f'viaje {viaje2.getLugarDestino(), viaje2.getFechaInicio()}.txt', viaje2)
archivo2.generarArchivo()
