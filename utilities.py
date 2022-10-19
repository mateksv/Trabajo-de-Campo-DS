# LIBRERIA DE utilities

import platform, os, random, string, signal, time

# CTRL + O - PARA HACER ZOOM

#-------------------------------------------------------------------------------------------------------
#   LIMPIAR PANTALLA
#-------------------------------------------------------------------------------------------------------
def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
#-------------------------------------------------------------------------------------------------------
#   CAMBIAR TITULO CMD
#-------------------------------------------------------------------------------------------------------
# os.system("Titulo nuevo")
def tituloConsola(titulo):
    comando = "title " + titulo
    os.system(comando)
#-------------------------------------------------------------------------------------------------------
#   CTRL+C 
#-------------------------------------------------------------------------------------------------------
# funcion handler
def handler(signum, frame):
    print("\nCtrl-C detectado. Finalizando la ejecucion...\n")
    time.sleep(0.2)
    exit()
# llamo a la funcion handler
def callHandler(): signal.signal(signal.SIGINT, handler)
#-------------------------------------------------------------------------------------------------------
#   GENERADOR DE CODIGOS
#-------------------------------------------------------------------------------------------------------
def codRand(tamanio_cadena):
    #tamanio_cadena = 5
    x = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(tamanio_cadena))
    return x
def codMayusRand(tamanio_cadena):
    #tamanio_cadena = 5
    x = "".join(random.choice(string.ascii_uppercase) for _ in range(tamanio_cadena))
    return x
def codMinusRand(tamanio_cadena):
    #tamanio_cadena = 5
    x = "".join(random.choice(string.ascii_lowercase) for _ in range(tamanio_cadena))
    return x
def codLetrasRand(tamanio_cadena):
    #tamanio_cadena = 5
    x = "".join(random.choice(string.ascii_letters) for _ in range(tamanio_cadena))
    return x
def codExaRand(tamanio_cadena):
    #tamanio_cadena = 5
    x = "".join(random.choice(string.hexdigits) for _ in range(tamanio_cadena))
    return x
def codNumRand(tamanio_cadena):
    #tamanio_cadena = 5
    x = "".join(random.choice(string.digits) for _ in range(tamanio_cadena))
    return x
#-------------------------------------------------------------------------------------------------------
# MANEJO DE ERRORES
#-------------------------------------------------------------------------------------------------------
def ManejoDeErrores(modulo):
    try:
        modulo
    except Exception as ex:
        print("\n>>>>> ERROR >>>>>", ex)
        input()
#-------------------------------------------------------------------------------------------------------
# MOSTRAR TITULO EN PANTALLA
#-------------------------------------------------------------------------------------------------------
def setTittle(titulo, char):
    l = len(titulo)
    print(char*l)
    print(titulo)
    print(char*l)
#-------------------------------------------------------------------------------------------------------
# OBJETO LISTA
#-------------------------------------------------------------------------------------------------------
class Lista():

    def __init__(self):
        '''Constructor'''
        self.list = []

    def getLista(self) -> list:
        '''Retorna la propia lista'''
        return self.list
        
    def addToList(self, elem):
        '''Agrega un elemento al final de la lista'''
        self.list.append(elem)

    def removePosList(list,pos):
        '''Elimina el elemento de la lista en la posicion pasada por parametro'''
        list.list.pop(pos)

    def removeElemList(self, elem):
        '''Elimina el elemento pasado por parametro de la lista'''
        self.list.remove(elem)

    def sortList(self):
        '''Ordena los elementos de la lista'''
        self.list.sort()

    def clearList(self):
        '''Elimina todos los elementos de la lista'''
        self.list.clear()

    def reverseList(self):
        '''Metodo .reverse()'''
        self.list.reverse()

    def copyList(listA: list) -> list:
        '''!!! Retorna una copia exacta de la lista????'''
        return listA.copy()

    def countElemList(self, elem):
        '''Retrona la cantidad de veces que aparece el elemento pasado por parametro en la lista'''
        return self.list.count(elem)

    def isEmpty(self) -> bool:
        '''Retorna True si la lista no tiene elementos'''
        return len(self.list)==0 

    def size(self) -> int:
        '''Retorna la cantidad de elementos de la lista'''
        return len(self.list)

    def exists(self, elem) -> bool:
        '''Retorna True o False si el elemento pasado por parametro pertenece a la lista'''
        return elem in self.list
#-------------------------------------------------------------------------------------------------------

