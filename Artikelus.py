import gender
import random


def seleccionar_palabra_aleatoria(nombre_archivo):
    with open( nombre_archivo, 'r' ) as f:
        palabras = list( f )

    return random.choice( palabras ).strip()
while True:




    palabra = seleccionar_palabra_aleatoria( 'nouns.txt')

    respuesta = input("¿Which is the gender of " + palabra + '?' + '\n')
    if respuesta == gender.get_gender_of_word(palabra):
        print("correct")
    else:
        print("No, it was: " + str(gender.get_gender_of_word(palabra)))