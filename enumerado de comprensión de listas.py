class ListaNumeros:
    def __init__(self, numeros):
        self.numeros = numeros

    def duplicar_numeros(self):
        return [(indice, numero * 2) for indice, numero in enumerate(self.numeros)]

# Crear una instancia de ListaNumeros
lista = ListaNumeros([1, 2, 3, 4, 5])

# Duplicar los números y enumerarlos
resultado = lista.duplicar_numeros()

print("Lista original:", lista.numeros)
print("Lista duplicada y enumerada:", resultado)
