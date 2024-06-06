import unittest

from models.viaje import Viaje
from models.tipoPago import tipoPago
from models.tipoGasto import tipoGasto
import time

class TestViaje(unittest.TestCase):

    def test_agregar_gasto_normal(self):
        viaje = Viaje('Estados Unidos', '2021-10-10', '2021-10-20', 1000000)
        viaje.agregarGasto('2021-10-10', 100, tipoPago.EFECTIVO, tipoGasto.COMPRAS)
        time.sleep(3)
        viaje.agregarGasto('2021-10-10', 300, tipoPago.EFECTIVO, tipoGasto.ALIMENTACION)
        time.sleep(3)
        viaje.agregarGasto('2021-10-10', 10, tipoPago.EFECTIVO, tipoGasto.ALOJAMIENTO)
        time.sleep(3)
        viaje.agregarGasto('2021-10-11', 10, tipoPago.EFECTIVO, tipoGasto.ALOJAMIENTO)
        time.sleep(3)
        viaje.agregarGasto('2021-10-11', 10, tipoPago.TARJETA, tipoGasto.ALOJAMIENTO)

        self.assertEqual(len(viaje.getGastos()), 5)

    def test_agregar_gasto_con_fecha_menor_inicial(self):
        viaje = Viaje('Estados Unidos', '2021-10-10', '2021-10-20', 1000000)
        with self.assertRaises(ValueError):
            viaje.agregarGasto('2021-10-09', 100, tipoPago.EFECTIVO, tipoGasto.COMPRAS)

    def test_agregar_gasto_con_fecha_mayor_final(self):
        viaje = Viaje('Estados Unidos', '2021-10-10', '2021-10-20', 1000000)
        with self.assertRaises(ValueError):
            viaje.agregarGasto('2021-10-21', 100, tipoPago.EFECTIVO, tipoGasto.COMPRAS)
