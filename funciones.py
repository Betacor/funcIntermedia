print("----------Desafío 1----------")



#1: Actualizar valores en diccionarios y listas

        # 1.Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
x = [ [5,2,3], [10,8,9] ] 

x[1][0] = 15
print(x)

        # 2.Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'}
]

estudiantes[0]['last_name'] = "Bryant"
print(estudiantes)


        # 3.En el directorio_deportes, cambia "Messi" por "Andrés".
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}

directorio_deportes['fútbol'][0] = 'Andrés'
print(directorio_deportes)

        # 4.Cambia el valor 20 en z a 30.
z = [ {'x': 10, 'y': 20} ]

z[0]['y'] = 30
print(z)



print("----------Desafío 2----------")



# 2: Iterar a través de una lista de diccionarios
# Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios, la función recorra cada diccionarios de la lista e imprima cada llave y el valor asociado. Por ejemplo, dada la siguiente lista:

estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

#1era Opción

def iterateDictionary(some_list):
    for x in range (len(some_list)):
        for key, val in some_list[x].items():
            print(key, " = ", val)

iterateDictionary(estudiantes)

# #2da Opción: first_name - Michael, last_name - Jordan
def iterateDictionary(some_list):
    for i in some_list:
        print(f"first_name - {i['first_name']}, last_name - {i['last_name']}")
    

iterateDictionary(estudiantes)



print("----------Desafío 3----------")



# 3: Obtener valores de una lista de diccionarios
# Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, la función imprima el valor almacenado en esa clave para cada diccionario. Por ejemplo, iterateDictionary2('name', estudiantes) debería generar:

# Michael
# John
# Mark
# KB

# #Y iterateDictionary2('last_name', estudiantes) debería generar:

# Jordan
# Rosales
# Guillen
# Tonel

estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary2(key_name, some_list):
    for i in range (len(some_list)):
        print(some_list[i][key_name])
            
iterateDictionary2('first_name', estudiantes)
iterateDictionary2('last_name', estudiantes)



print("----------Desafío 4----------")



#4: Iterar a través de un diccionarios con valores de lista

# #Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todos listas, imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores asociados dentro de la lista de cada clave. Por ejemplo:

# printInfo(dojo)
# # salida:
# # 7 UBICACIONES
# # San Jose
# # Seattle
# # Dallas
# # Chicago
# # Tulsa
# # DC
# # Burbank

# 8 INSTRUCTORES
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh

dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for i in (some_dict):
        print(len(some_dict[i]),i)
        for j in some_dict[i]:
            print(j)    

printInfo(dojo)
