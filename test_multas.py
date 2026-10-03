import unittest

from multas import calcular_multa


class PruebasDeMulta(unittest.TestCase):
    def test_cero_dias_no_genera_multa(self):
        self.assertEqual(calcular_multa(0), 0)

    def test_tres_dias_generan_seis_quetzales(self):
        self.assertEqual(calcular_multa(3), 6)

    def test_quince_dias_respetan_el_limite(self):
        self.assertEqual(calcular_multa(15), 20)

    def test_dias_negativos_generan_error(self):
        with self.assertRaises(ValueError):
            calcular_multa(-2)


if __name__ == "__main__":
    unittest.main()
