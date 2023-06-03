#BUSQUEDA DE CANTIDAD DE COMPUESTOS EN INVENTARIO 
#Para realizar las busqueda en el inventario es necesario instalar algunas librerias para Python. 
#Ingresa el siguiente codigo en tu terminal para instalar las librerias:
#pip install pandas
#pip install openpyxl
#NOTA: OBVIAMENTE TIENES QUE TENER INSTALADO PYTHON PARA EJECUTAR CODIGO DE PYTHON EN TU TERMINAL

#Para abrir el archivo de Excel con el inventario debes de tenerlo guardado en la misma carpeta que este script.

#Para poder hacer uso de las librerias que acabamos de descargar, lo vamos a importar:
import pandas as pd
#Esta libreria te ayuda a abrir y editar archivos de excel con python
#Para leer el inventario
inventario = pd.read_excel(r'C:\Users\javie\Desktop\Python\inv.xlsx')  #Aqui va la ruta del archivo excel
df=pd.DataFrame(inventario) #guardamos como dataframe el excel
df['Nombre']=df['Nombre'].str.lower()
#print(df.to_string(index=False))
#puedes descomentar la linea de arriba para imprimir el documento de excel 

compuesto=input('Escribe el nombre del compuesto: ')

cantidad=df.loc[df['Nombre']==compuesto]['Cantidad']

noindice=[''] * len(cantidad)   #estas dos lineas son para imprimir el dataframe sin el indice y sea mas estetico, para ello el indice se convierte en una matriz vacia
cantidad.index=noindice
print ('La cantidad del compuesto es: ', cantidad.to_string()) #imprimmos como str por estetica

gaveta=df.loc[df['Nombre']==compuesto]['Gaveta']  
noindice=[''] * len(gaveta)
gaveta.index=noindice
print ('Se encuentra en la gaveta: ', gaveta.to_string())




