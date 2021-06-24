import random
import nltk


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#import numpy as np

# Leyendo el archivo con nombre articulo
def leer():
    with open('article/archivo.txt', mode='r', encoding='utf-8-sig') as f:
        articulo = f.read()
    return articulo

Nombre_Bot = "Fantastics"


def Obtener_respuesta(sms):
    salidaListas = ['chau', 'nos vemos', 'me voy']

    while(True):
        #entrada = input()
        if sms.lower() in salidaListas:
            return "Hasta Luego"
        else:
            # Buscar el saludo
            if respuestaSaludo(sms) != None:
                return respuestaSaludo(sms)
                
            # Cuando NO exise el saludo, procesamos texto
            else:
                return respuestaChatbot(sms)
                

# Función que retornara un saludo al usuario
def respuestaSaludo(texto):
    texto = texto.lower()
    # Respuesta de saludo del chatbot
    saludos = ['hola','que tal','buen día','dime','como estas', 'como vas', 'hey', 'señor']
    #for palabra in texto.split():
    if texto in saludos:
        return random.choice(saludos)

# Funcion que ordena la linta conforme al indice
def ordenarIndice(lista):
    tamaño = len(lista)
    indiceLista = list(range(0, tamaño))
    x = indiceLista
    for i in range(tamaño):
        for j in range(tamaño):
            if x[indiceLista[i]] > x[indiceLista[j]]:
                aux = indiceLista[i]
                indiceLista[i] = indiceLista[j]
                indiceLista[j] = aux
    return indiceLista

# Función para crear la respuesta del Chatbot
def respuestaChatbot(entradaUsuario):
    # Leemos el articulo
    articulo = leer()
    # Listamos en oraciones el contenido de articulo
    listaOraciones = nltk.sent_tokenize(articulo)
    # Convertimos en minuscula la entrada de texto que ingreso el usuario
    entradaUsuario = entradaUsuario.lower()
    # Esta entrada del usuario, agregamos al final de la lista
    listaOraciones.append(entradaUsuario)
    # Creamos el diccionario con la bolsa de palabras, vectorizado
    CV = CountVectorizer().fit_transform(listaOraciones)
    # Esta función nos ayuda a comparar la similitud entre matrices
    similitudPuntuacion = cosine_similarity(CV[-1], CV)
    # A traves de la funcion flatten, convertimos a un array simple, para procesar
    similitudPuntuacionLista = similitudPuntuacion.flatten()
    # Llamamos a la funcion ordenar indice
    indice = ordenarIndice(similitudPuntuacionLista)
    indice = indice[1:]

    respuestaChatbot001 = ''
    respuestas = 0
    # Buscamos la mayor similitud y el contenido de esto agregamos a respuesta chatbot001 
    for i in range(len(indice)):
        if similitudPuntuacionLista[indice[i]] > 0.0:
            respuestaChatbot001 = respuestaChatbot001 + ' ' + listaOraciones[indice[i]]
            respuestas = 1
            break 
    # En caso no se encuentre la respuesta
    if respuestas == 0:
        respuestaChatbot001 = respuestaChatbot001 + ' ' + 'No entiendo'
        return respuestaChatbot001
        
    listaOraciones.remove(entradaUsuario)

    return respuestaChatbot001
