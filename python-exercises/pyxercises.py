# 1) Función que calcula el máximo común divisor entre dos números:
def mcd(x, y):
    """
    El máximo común divisor de dos o más números enteros es el mayor número entero que los divide sin dejar residuo alguno.
    Si y==0 → MCD = x;
    Si y!=0 → la función se llama recursivamente con y & el resto de la división entre x e y; 
    El proceso continúa hasta que y sea cero, momento en el que se devuelve x como el MCD.
    """

    if y == 0:
        return x
    
    return mcd(y, x % y)

x = 9 # 9/3 es 3, con 0 residuo
y = 3 # 3/3 es 1, con 0 residuo
z = mcd(x, y)
print(z)

x = 45 # 45/5 es 9, con 0 residuo
y = 20 # 20/5 es 4, con 0 residuo
z = mcd(x, y)
print(z)

# 2) Función que calcula el mínimo común múltiplo entre dos números:

def mincm(x, y):
    """
    El mínimo común múltiplo de dos o más números naturales es el menor múltiplo común de todos ellos.
    """
    # Paso1) Calcular máximo común divisor
    maxcd = mcd(x, y) # función mcd definida en el ejercicio1

    # Paso2) Calcular el mínimo común múltiplo utilizando la siguiente fórmula:
    mincm = (x * y) / maxcd

    return mincm

x = 46
y = 32
z = mincm(x, y)
print(z) # 736

# 3) Escribe un programa que reciba una cadena de caracteres,
# devuelva un diccionario con cada palabra que contiene 
# y la cantidad de veces que aparece (frecuencia)

def word_count(cadena):
    """
    # 1) El programa word_counter convierte la cadena de caracteres en una lista de palabras utilizando el método split(); 
    # → El método split() en Python es una función de cadena (string) que divide una cadena en una lista de subcadenas basadas en un separador especificado; sin argumentos, divide la cadena en una lista de subcadenas basadas en cualquier espacio en blanco en la cadena.
    # 2) Luego, inicializa un diccionario vacío para almacenar la frecuencia de cada palabra;
    # 3) Recorre la lista de palabras, actualizando la frecuencia de cada una en el diccionario utilizando una estructura condicional.
    """
    # Convierte la cadena en una lista de palabras
    word_list = cadena.split()

    # Inicializa un diccionario vacío para almacenar la frecuencia de cada palabra
    word_freq = {}

    # Recorre la lista de palabras & actualiza la frecuencia de cada una en el diccionario
    for word in word_list:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return word_freq

# Llamada:
cadena = "Mis colores favoritos son el blanco & el rosa." # cadena de caracteres a analizar
freq = word_count(cadena)
print(freq) # {'Mis': 1, 'colores': 1, 'favoritos': 1, 'son': 1, 'el': 2, 'blanco': 1, '&': 1, 'rosa.': 1}

# 4) Función que recibe una cadena de caracteres & devuelve un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia).
# Luego, otra función que recibe el diccionario generado con la función anterior & devuelve una tupla con la palabra más repetida y su frecuencia.

# Función definida en el ejercicio 3:
def word_count(cadena):
    """
    Recibe una cadena de caracteres & devuelve un diccionario con la frecuencia de cada palabra.
    """
    # Convierte la cadena en una lista de palabras
    word_list = cadena.split()

    # Inicializa un diccionario vacío para almacenar la frecuencia de cada palabra
    word_freq = {}

    # Recorre la lista de palabras & actualiza la frecuencia de cada una en el diccionario
    for word in word_list:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return word_freq

# Función que recibe el diccionario generado por la función anterior y devuelve una tupla con la palabra más repetida y su frecuencia:
def most_repeated_word(dictionary):
    """
    Recibe un diccionario con la frecuencia de cada palabra & devuelve una tupla con la palabra más repetida y su frecuencia.
    """
    # Inicializa las variables que almacenarán la palabra más repetida y su frecuencia:
    most_repeated_word = ""
    most_repeated_freq = 0

    # Recorre el diccionario & actualiza la palabra más repetida y su frecuencia, en caso necesario:
    for word, freq in dictionary.items():
        if freq > most_repeated_freq:
            most_repeated_word = word
            most_repeated_freq = freq

    # Devuelve una tupla con la palabra más repetida y su frecuencia:
    return (most_repeated_word, most_repeated_freq)

# Llamada a la función word_count con la cadena de caracteres;
# el diccionario resultante se almacena en la variable freq;
# Se llama a la función most_repeated_word con el diccionario freq;
# se guarda la palabra más repetida y su frecuencia en las variables word & freq;
# Finalmente, se imprime un mensaje que muestra la palabra más repetida y su frecuencia.
cadena = "Mi gata de 7 años es muy activa & mi gata de 13 años mucho más tranquila."
freq = word_count(cadena)
word, freq = most_repeated_word(freq)
print(f"La palabra más repetida es '{word}' con una frecuencia de {freq}.") # La palabra más repetida es 'gata' con una frecuencia de 2.

# 5) Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una cadena de texto en su valor númerico, escribe una función get_int() que lea un valor entero del usuario & lo devuelva, iterando mientras el valor no sea correcto. Resuelve el ejercicio de manera iterativa y recursiva.

# El bloque try-except es un medio (de tantos) para capturar la excepción ValueError que se produce cuando el usuario ingresa un valor que no se puede convertir a un número entero.

# Función iterativa:
# Esta función utiliza un bucle while que se ejecuta indefinidamente hasta que el usuario ingrese un valor que se pueda convertir a un número entero; 
# Dentro del bucle, se intenta leer un valor entero utilizando la función input() & se intenta convertir el resultado a un número entero utilizando la función int();
# Si la conversión es correcta, el valor entero se devuelve y la función termina;
#  Si se produce una excepción ValueError, se imprime un mensaje de error & se vuelve a pedir al usuario que ingrese un valor.
def get_int():
    """
    Esta función lee un valor entero del usuario y lo devuelve, iterando mientras el valor no sea correcto.
    """
    while True:
        try:
            user_value = int(input("Ingresa un número entero: "))
            return user_value
        except ValueError:
            print("El número que has ingresado no es entero.")
get_int()

# Función recursiva:
# Dentro de la función, se intenta leer un valor entero utilizando la función input() 
# y se intenta convertir el resultado a un número entero utilizando la función int();
#  Si la conversión es correcta, el valor entero se devuelve; 
# Si se produce una excepción ValueError, se imprime un mensaje de error & se llama a la misma función de nuevo para volver a intentar leer un valor entero del usuario.
def get_int():
    """
    Esta función lee un valor entero del usuario y lo devuelve, iterando mientras el valor no sea correcto.
    """
    try:
        user_value = int(input("Ingresa un número entero: "))
        return user_value
    except ValueError:
        print("El número que has ingresado es incorrecto.")
        return get_int()
get_int()

# 6) Crea una clase llamada Persona:
# Sus atributos son: nombre, edad y DNI. 
# Construye los siguientes métodos para la clase: 
# 1) un constructor, donde los datos pueden estar vacíos. 
# 2) los setters y getters para cada uno de los atributos. Validar las entradas de datos. 
# 3) mostrar(): muestra los datos de la persona. 
# 4) es_mayor_de_edad(): devuelve un valor lógico indicando si es mayor de edad.

# El método '__init__' es el constructor de la clase y se utiliza para inicializar los atributos de la instancia.
# Los getters y setters se utilizan para acceder & modificar los atributos de la clase, respectivamente.
# En cada uno de los setters, se valida que el valor ingresado sea del tipo y formato adecuado, lanzando una excepción ValueError si no es así.
# El método 'mostrar' se utiliza para imprimir en pantalla los datos de la persona.
# El método 'es_mayor_de_edad' devuelve un valor lógico indicando si la persona es mayor de edad o no.

class Persona:
    def __init__(self, nombre='', edad=0, dni=''):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni

    # getters y setters para Nombre:
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self._nombre = nombre
        else:
            raise ValueError("El nombre debe ser una cadena de texto")

    # getters y setters para Edad:
    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self._edad = edad
        else:
            raise ValueError("La edad debe ser un número entero positivo")

    # getters y setters para DNI:
    def get_dni(self):
        return self._dni

    def set_dni(self, dni):
        if isinstance(dni, str) and len(dni) == 9 and dni.isnumeric():
            self._dni = dni
        else:
            raise ValueError("El DNI debe ser una cadena de texto de 9 dígitos numéricos")

    def mostrar(self):
        print(f"Nombre: {self._nombre}, Edad: {self._edad}, DNI: {self._dni}")

    def es_mayor_de_edad(self):
        return self._edad >= 18

p = Persona()
p.set_nombre('Ámbar')
p.set_edad(25)
p.set_dni('123456789')
p.mostrar()
print(p.es_mayor_de_edad())
# Este código crea una instancia de la clase 'Persona', 
# establece sus atributos utilizando los setters, 
# uestra los datos de la persona 
# y determina si es mayor de edad o no.

# 7) Crea una clase llamada Cuenta que tendrá los siguientes atributos: 
# titular (que es una persona) 
# y cantidad (puede tener decimales). 
# El titular será obligatorio y la cantidad será opcional. 
# Crear los siguientes métodos para la clase: 
# 1) un constructor, donde los datos pueden estar vacíos. 
# 2) los setters y getters para cada uno de los atributos; 
# El atributo no se puede modificar directamente, sólo ingresando o retirando dinero. 
# 3) mostrar(): muestra los datos de la cuenta.
# 4) ingresar(cantidad): se ingresa una cantidad a la cuenta; 
# si la cantidad introducida es negativa, no se hará nada. 
# 5) retirar(cantidad): se retira una cantidad a la cuenta. 
# La cuenta puede estar en números rojos.

class Cuenta:
    
    def __init__(self, titular, cantidad=0):
        self.__titular = titular
        self.__cantidad = cantidad
    
    def get_titular(self):
        return self.__titular
    
    def set_titular(self, titular):
        self.__titular = titular
        
    def get_cantidad(self):
        return self.__cantidad
    
    def mostrar(self):
        print(f"Titular: {self.__titular.mostrar()}, Cantidad: {self.__cantidad}")
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
    
    def retirar(self, cantidad):
        self.__cantidad -= cantidad

# En la clase Cuenta, el atributo titular es de la clase Persona, por lo que es necesario crear primero la clase Persona con sus atributos y métodos correspondientes.
# Para evitar que el atributo cantidad sea modificado directamente desde fuera de la clase, se utiliza una convención de Python donde los atributos se escriben con doble guión bajo (__) delante; Ésto los convierte en atributos privados y sólo se pueden acceder a ellos a través de los métodos de la clase.

# 8) Vamos a definir ahora una "CuentaJoven", creando una nueva clase CuentaJoven, 
# que derive de la clase que me has creado en tu respuesta anterior. 
# Cuando se crea ésta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. 
# Crear los siguientes métodos para la clase: 
# 1) un constructor. 
# 2) los setters y getters para el nuevo atributo. 
# 3) en ésta ocasión los titulares de éste tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años, y falso en caso contrario. 
# 4) además, la retirada de dinero sólo se podrá hacer si el titular es válido. 
# 5) el método mostrar() debe devolver el mensaje de "Cuenta Joven" y la bonificación de la cuenta.

class CuentaJoven(Cuenta):
    
    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion
    
    def get_bonificacion(self):
        return self.__bonificacion
    
    def set_bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion
        
    def es_titular_valido(self):
        return self.get_titular().es_mayor_de_edad() and self.get_titular().get_edad() < 25
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("Titular no válido para realizar la operación")
    
    def mostrar(self):
        print(f"Cuenta Joven. Bonificación: {self.__bonificacion}")

# La clase CuentaJoven hereda de la clase Cuenta;
# Agrega el atributo bonificacion 
# y los métodos es_titular_valido & retirar. 
# En el método retirar se verifica si el titular es válido antes de realizar la operación. 
# En el método mostrar se muestra el mensaje de "Cuenta Joven" y la bonificación correspondiente.



