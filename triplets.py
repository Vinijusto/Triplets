import sys
import json

contador_secuencias = {} #{triplet: cantidad de ocurrencias}
def analyze_secuencia(secuencia):#analiza la secuencia(lista de paginas), para ponerlo dentro de un diccionario y contabilizar los triplets
    cant_visitas = len(secuencia)
    aux=''
    
    for i in range(cant_visitas - 2):  
        for l in range(i,i + 3):
            aux += secuencia[l]
        if aux not in contador_secuencias:
            contador_secuencias[aux] = 1
        else:
            contador_secuencias[aux] += 1
        aux = ''
    
    return

id_user = 'user1' 
secuencia = []#es una variable auxiliar en la que se ira agregando las paginas visitadas por cada usuario
count = 1
f = open("log_file.txt","r")

while(count <= 500): #este loop sirve para analizar renglon a renglon el log_file
    linea = f.readline().split(';')
    pag = linea[2].strip() #el valor de la variable 'pag' es la pagina visitada por el usuario en la linea que se analiza
    if linea[0] != id_user: #consulta si el usuario del renglon cambio o sigue siendo el mismo al anterior
        analyze_secuencia(secuencia)
        id_user = linea[0]#se actualiza el id_user al actual
        secuencia.clear() #se vacia la lista ya que hubo cambio de usuario
    
    secuencia.append(pag)
    count += 1
contador_secuencias_ordenado =  dict(sorted(contador_secuencias.items(), key=lambda item: item[1],reverse=True))#codigo para ordenar los items del diccionario de mayor a menor
json.dump(contador_secuencias_ordenado, open('dev_integrated.json', 'w'), sort_keys=False, indent=4, separators=(',', ': '))# un json completo de todos los triplets
