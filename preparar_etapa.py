from pathlib import Path
import sys


CARPETA = Path(__file__).parent

IMPLEMENTACIONES = {
    1: '''def calcular_multa(dias):
    """Calcula la multa inicial: Q2 por cada día de atraso."""
    return dias * 2
''',
    2: '''def calcular_multa(dias):
    """Cambio incorrecto conservado para mostrar una regresión."""
    return 20
''',
    3: '''def calcular_multa(dias):
    """Calcula Q2 por día, con un máximo de Q20."""
    return min(dias * 2, 20)
''',
    4: '''def calcular_multa(dias):
    """Aún no valida días negativos; esta etapa muestra el incidente."""
    return min(dias * 2, 20)
''',
    5: '''def calcular_multa(dias):
    """Calcula la multa y rechaza días negativos."""
    if dias < 0:
        raise ValueError("los días de atraso no pueden ser negativos")
    return min(dias * 2, 20)
''',
}

PRUEBAS = {
    1: '''import unittest

from multas import calcular_multa


class PruebasDeMulta(unittest.TestCase):
    def test_cero_dias_no_genera_multa(self):
        self.assertEqual(calcular_multa(0), 0)

    def test_tres_dias_generan_seis_quetzales(self):
        self.assertEqual(calcular_multa(3), 6)

    def test_quince_dias_respetan_el_limite(self):
        self.assertEqual(calcular_multa(15), 30)


if __name__ == "__main__":
    unittest.main()
''',
    2: '''import unittest

from multas import calcular_multa


class PruebasDeMulta(unittest.TestCase):
    def test_cero_dias_no_genera_multa(self):
        self.assertEqual(calcular_multa(0), 0)

    def test_tres_dias_generan_seis_quetzales(self):
        self.assertEqual(calcular_multa(3), 6)

    def test_quince_dias_respetan_el_limite(self):
        self.assertEqual(calcular_multa(15), 20)


if __name__ == "__main__":
    unittest.main()
''',
    3: '''import unittest

from multas import calcular_multa


class PruebasDeMulta(unittest.TestCase):
    def test_cero_dias_no_genera_multa(self):
        self.assertEqual(calcular_multa(0), 0)

    def test_tres_dias_generan_seis_quetzales(self):
        self.assertEqual(calcular_multa(3), 6)

    def test_quince_dias_respetan_el_limite(self):
        self.assertEqual(calcular_multa(15), 20)


if __name__ == "__main__":
    unittest.main()
''',
    4: '''import unittest

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
''',
    5: '''import unittest

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
''',
}


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in {str(numero) for numero in range(1, 6)}:
        print("Uso: python preparar_etapa.py N, donde N es un número del 1 al 5.")
        return 2

    etapa = int(sys.argv[1])
    (CARPETA / "multas.py").write_text(IMPLEMENTACIONES[etapa], encoding="utf-8")
    (CARPETA / "test_multas.py").write_text(PRUEBAS[etapa], encoding="utf-8")
    print(f"Etapa {etapa} activada.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
