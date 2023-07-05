"""Type, Comprensión de Listas, Sorted y Filter."""

from typing import List, Union


def numeros_al_final_basico(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Toma una lista de enteros y strings y devuelve una lista con todos los
    elementos numéricos al final.
    """
    lista3 = []
    lista2 = []
    for i in range(len(lista)):
      if isinstance(lista[i], int):
        lista3.append(lista[i])
      else :
        lista2.append(lista[i])
    return lista2 + lista3



# NO MODIFICAR - INICIO
assert numeros_al_final_basico([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN
print numeros_al_final_basico([3, "a", 1, "b", 10, "j"])

###############################################################################


def numeros_al_final_comprension(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando comprensión de listas."""
    lista3 = []
    lista2 = []
    for i in range(len(lista)):
      if isinstance(lista[i], int):
        lista3.append(lista[i])
      else :
        lista2.append(lista[i])
    return lista2 + lista3


# NO MODIFICAR - INICIO
assert numeros_al_final_comprension([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_sorted(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """Re-escribir utilizando la función sorted con una custom key.
    Referencia: https://docs.python.org/3/library/functions.html#sorted
    """

    return sorted(lista, key= lambda x : isinstance(x, str))


# NO MODIFICAR - INICIO
assert numeros_al_final_sorted([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_filter(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir utilizando la función filter.
    Referencia: https://docs.python.org/3/library/functions.html#filter
    """
    numeros = list(filter(lambda x: isinstance(x, int), lista))
    no_numeros = list(filter(lambda x: not isinstance(x, int), lista))
    return no_numeros + numeros


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_filter([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN


###############################################################################


def numeros_al_final_recursivo(lista: List[Union[float, str]]) -> List[Union[float, str]]:
    """CHALLENGE OPCIONAL - Re-escribir de forma recursiva."""
    # Caso base: la lista está vacía
    if not lista:
        return []

    # Verificar el primer elemento de la lista
    if isinstance(lista[0], int):
        # Si es numérico, llamamos recursivamente con el resto de la lista y agregamos el primer elemento al final
        return numeros_al_final_recursivo(lista[1:]) + [lista[0]]
    else:
        # Si no es numérico, llamamos recursivamente con el resto de la lista y mantenemos el primer elemento
        return [lista[0]] + numeros_al_final_recursivo(lista[1:])


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    assert numeros_al_final_recursivo([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
# NO MODIFICAR - FIN
