import math

def esPrimo(numero):
    for i in range(2, round(math.sqrt(numero)) + 1):
        if (numero % i == 0):
            return True
    return False
Intermedio = ""

class Lista(Intermedio):
    def __init__(self, lista):
        self.lista = lista

    def presentarLista(self):
        for elemento in self.lista:
            print(elemento)

    def buscarLista(self, valor):
        for elemento in self.lista:
            if (elemento == valor):
                print(valor)

    def listaFactorial(self):
        lista = []
        for elemento in self.lista:
            lista.append(math.factorial(elemento))
        return lista

    def listaPrimo(self):
        lista = []
        for elemento in self.lista:
            if (esPrimo(elemento)):
                lista.append(elemento)
        return lista

    def listaNotas(self, listaNotasDicccionario):
        for key in listaNotasDicccionario.keys():
            print(key)
            for nota in listaNotasDicccionario[key]:
                print(nota, end="")
            print("")

    def insertarLista(self, valor, posicion):
        self.lista.insert(posicion, valor)

    def eliminarLista(self, valor):
        veces = self.lista.count(valor)
        for i in range(veces):
            self.lista.remove(valor)

    def retornaValorLista(self, posicion):
        return self.lista.pop(posicion)

    def copiarTuplaLista(self, tupla):
        self.lista.extend(tupla)

    def vueltoLista(self, listaClientesDiccionario):
        for key in listaClientesDiccionario.keys():
            print(key)
            tmp = 0
            for gasto in listaClientesDiccionario[key]:
                tmp += gasto
            print(tmp)

    def retornaValor(self, posicion):
        return self.lista.pop(posicion)