
def calcular_total(valor, desconto):
    if desconto < 0 or desconto > 100:
        raise ValueError("Desconto inválido")

    return valor * (1 - desconto / 100)
