def calcular_multa(dias):
    """Calcula Q2 por día, con un máximo de Q20."""
    return min(dias * 2, 20)
