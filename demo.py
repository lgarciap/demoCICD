import sys

from multas import calcular_multa


COLOR = sys.stdout.isatty()


def colorear(texto, codigo):
    if not COLOR:
        return texto
    return f"\033[{codigo}m{texto}\033[0m"


def mostrar_multa(multa):
    if multa < 0:
        return f"-Q{abs(multa)}"
    return f"Q{multa}"


def mostrar_encabezado():
    print()
    print(colorear("+------------------------------------------+", "36"))
    print(colorear("|       BIBLIOTECA: CALCULADORA DE MULTAS |", "36"))
    print(colorear("+------------------------------------------+", "36"))
    print("  Tarifa: Q2 por día de atraso")
    print("  Escriba 'salir' para terminar la demostración.")
    print()


def main():
    mostrar_encabezado()

    while True:
        entrada = input("Días de atraso: ").strip()
        if entrada.lower() == "salir":
            print()
            print(colorear("[FIN] Demostración terminada.", "36"))
            return

        try:
            dias = int(entrada)
            multa = calcular_multa(dias)
        except ValueError as error:
            if entrada.lstrip("-").isdigit():
                print(colorear(f"[ERROR] {error}", "31"))
            else:
                print(colorear("[ERROR] Escriba un número entero de días.", "31"))
            continue

        print(colorear(f"[RESULTADO] La multa es {mostrar_multa(multa)}.", "32"))


if __name__ == "__main__":
    main()
