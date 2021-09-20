import sys
import random
""" Este codigo es unico y exclusivamente dedicado a crear el log file, con una interaccion de 6 paginas y una determinada cantidad de usuarios alaeatorios, con un total de 500 logs,
    el numero 500 lo elegi para hacer un analisis mas amplio y que haya mas apariciones"""
user = 1
aux = 0
randomchange = random.randint(3,7) #La funcion random.randint() genera un numero aleatorio entre dos parametros, el primero el menor valor del numero y el segundo el mayor que se puede obtener.
f = open("log_file.txt","w")         #Por otra parte el randomchange, determina cuando un usuario va a dejar de ser analizado, osea cambia el user en el logfile
for i in range(1,501):
    if aux == randomchange:
        aux = 0
        user += 1 #cambio de usuario
        randomchange = random.randint(3,7)
    line = 'user' + str(user) + ';time' + str(i) + ';page_' + str(random.randint(1,6)) + '\n'#esta anteultima suma determina que pagina visitar el usuario
    f.write(line)
    aux += 1
f.close()