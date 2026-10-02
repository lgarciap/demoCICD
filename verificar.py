import sys
import unittest

import test_multas


def main():
    suite = unittest.defaultTestLoader.loadTestsFromModule(test_multas)
    resultado = unittest.TextTestRunner(verbosity=2).run(suite)

    if resultado.wasSuccessful():
        print("Verificación aprobada.")
        return 0

    print("Verificación fallida.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
