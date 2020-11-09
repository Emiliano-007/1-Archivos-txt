from io import open

#entrada de datos
entrada=input("Escribe: ")
#alamacenar el fichero para escribir
fichero1=open('ejemplo.txt','w')
fichero1.write(entrada)
#Se cierra el fichero
fichero1.close()
input()



# Ruta de donde lerremos el fichero, r indica lectura (por efecto ya es r)
fichero=open('ejemplo.txt','r')
# Lectura completa
texto=fichero.read()
#cerramos el fichero
fichero.close()
print(texto)
