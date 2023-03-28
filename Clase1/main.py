import pandas as pd
import matplotlib.pyplot as plt
inmuebles = pd.read_csv('inmuebles_bogota.csv')  #lectura del archivo csv comma separate value
print("Primeras 5 filas del objeto:")
print(inmuebles.head()) #mostar las 5 primeras filas del dataset
print("Filas x columnas del objeto:")
print(inmuebles.shape)#muestra la forma del objeto, el indice no se contabiliza como columna
print("Encabezados del objeto:")
print(inmuebles.columns)#información acerca de las columnas
print("Cambiando el nombre de los encabezados")
columnas = {'Baños':'Banhios','Área':'Area'}#no es necesario para el valor de todas las columnas, solo las que queremos cambiar
inmuebles=inmuebles.rename(columns=columnas)#cambiando nombres con caracteres especiales para evitar problemas en el futuro
print(inmuebles.columns) #evidencia que funciona
print(inmuebles.sample(10))#filas con indices de forma aleatoria
print(inmuebles.info())#toda la información del DataFrame
print(inmuebles.iloc[300])#para ver la fila con el indice especificado, se hace referencia al indice 301
print(inmuebles.iloc[300:305])#una parte del objeto
print(inmuebles['Valor'][300])#solo un dato especificado
print(inmuebles['Valor'][300:305])#una porción de un solo tipo de dato, y eso es un pandas.core.series.Series, es como un array, pero de Pandas
print(inmuebles.Area.mean())#area promedio de todo el objeto
print(inmuebles.sample(100))#una muestra del objeto
print(inmuebles.Barrio=='Chico Reservado') #muestra que filas tengan una igualda con el barrio seleccionado
print(sum(inmuebles.Barrio=='Chico Reservado'))#cantidad total de filas donde haya un inmueble en el barrio seleccionado
inmuebles_chico=inmuebles.Barrio=='Chico Reservado'#mascara de Pandas
print(type(inmuebles_chico))#se observa que es un pandas.core.series.Series
chico_reservado=inmuebles[inmuebles_chico]#aplicar la mascara a nuestro antiguo dataframe para crear otro dataframe
print(chico_reservado)#nuevo dataframe
#calcular el promedio de area en chico reservado
print(chico_reservado.Area.mean())
#cantidad de barrios en nuestros dataset
print(len(inmuebles.Barrio.value_counts()))#cantidad de barrios
print(inmuebles.Barrio.value_counts())#cantidad de inmuebles por cada barrio
print(len(inmuebles.UPZ.value_counts()))#cantidad de UPZ's
#creación de gráficos
inmuebles_barrio=inmuebles.Barrio.value_counts()#nuevo dataframe
inmuebles_barrio_podio=inmuebles.Barrio.value_counts().head(10)#dataframe con los primeros 10 de orden descendente
#esto es para google colab
#inmuebles_barrio.head(10).plot.bar()#barr==grafico de barras, con head es la cantidad de datos que quisiera
#esto es para VS Code
inmuebles_barrio_podio.plot(kind='bar', x='columna_x', y='columna_y')#creamos grafico de barras
plt.show()#mostramos grafico
