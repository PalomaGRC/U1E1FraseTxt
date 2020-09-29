#Abrimos archivo
archivo = open("Oracionpy.txt","r") #Abrimos el archivo txt
texto = archivo.read().split(',') #Separamos en palabras la cadena concatenada, el delimitador es ','
print("El texto del archivo es",texto)#Imprimos en pantalla el contenido del txt

correcto = ['Por que','al', 'perrito','le','duele','la','muela','?']#Orden correcto de la oracion, respuesta a la pregunta en programa java xd

archivo = open("Oracionpy.txt","r")#Abrimos el archivo txt
textoaux = archivo.read().split(',')#Separamos en palabras la cadena concatenada, el delimitador es ','
aux = "" #Creamos un auxiliar

#Ordenamos el arreglo
for i in range(0, len(texto)):
    for j in range(0, len(texto)):
        if texto[i] == correcto[j]:#Si la palabra del arreglo "texto" en posicion i coincide con la palabra del arreglo "correcto" posición j..
            textoaux[j] = correcto[j]#El arreglo "textoaux" posicion j almacena la palabra que esta en el arreglo "correcto" evaluada en ese momento

#Imprimimos el arreglo ordenado
for i in range(0, len(texto)):
       aux = aux + textoaux[i]#Guardamos cada palabra almacenada en el arreglo "textoaux" en el aux creado anteriormente
       aux = aux + " "#Entre cada palabra colocamos un espacio en blanco, para que no estén juntas

print("El texto ordenado: ", aux)#Mostramos la cadena en pantalla ordenada

