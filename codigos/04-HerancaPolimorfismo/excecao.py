def processar_nota(valor):
    try:
        nota = float(valor)

        if nota < 0 or nota > 10:
            raise ValueError("A nota deve estar entre 0 e 10.")

    except ValueError as e:
        raise ValueError(
            f"Erro ao processar a nota '{valor}'."
        ) from e

    else:
        print(f"Nota processada: {nota}")
        return nota

    finally:
        print("Processamento encerrado.")


notas = ["8.5", "7.0", "abc", "11"]

for valor in notas:
    try:
        nota = processar_nota(valor)
        print(f"Nota válida: {nota}\n")

    except ValueError as e:
        print(f"Erro: {e}\n")