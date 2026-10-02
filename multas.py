def calcular_multa(dias):
    """Calcula la multa y rechaza días negativos."""
    if dias < 0:
        raise ValueError("los días de atraso no pueden ser negativos")
    return min(dias * 2, 20)
