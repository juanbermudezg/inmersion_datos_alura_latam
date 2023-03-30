#Promedio de área de todos los inmuebles en los barrios en el dataset. El top 10.
import pandas as pd
import matplotlib.pyplot as plt
inmuebles = pd.read_csv('inmuebles_bogota.csv') 
columnas = {'Baños':'Banhios','Área':'Area'}
inmuebles=inmuebles.rename(columns=columnas)
#a=inmuebles_barrio=inmuebles.Barrio.value_counts()#nuevo dataframe
cantidadBarrios=len(inmuebles.Barrio.value_counts())
#print(inmuebles['Barrio'])
inmuebles_barrio=inmuebles.Barrio.value_counts()
top10=pd.DataFrame({'Barrio':[],'Area':[]})
for i in range(0,len(inmuebles_barrio)):
    indices=inmuebles_barrio.index[i]
    inmuebles_temp=inmuebles.Barrio==indices
    barrio_temp=inmuebles[inmuebles_temp]
    areaTemp=barrio_temp.Area.mean()
    nuevaFila=pd.Series({'Barrio':indices,'Area':areaTemp})
    top10.loc[len(top10)] = nuevaFila
top10=top10.sort_values(by='Area', ascending=False).head(10)
#print(top10.head(10))
plt.plot(top10['Barrio'], top10['Area'])
plt.xlabel('Barrios')
plt.xticks(rotation=90)
plt.ylabel('Area m^2')
#plt.show()
#Consultar otros datos estadísticos, conteo, mediana, valores mínimo y máximo.
#Comenzamos con habitaciones
conteo = inmuebles.count() #contamos cantidad de datos en general
print(conteo)
print("-------------Habitaciones--------------")
medianaHabitaciones = inmuebles['Habitaciones'].median() #mediana de habitaciones
print(medianaHabitaciones)
minimoHabitaciones = inmuebles['Habitaciones'].min()#valor minimo de habitaciones
print(minimoHabitaciones)
maximoHabitaciones = inmuebles['Habitaciones'].max()#valor maximo de habitaciones
print(maximoHabitaciones)
mediaHabitaciones=inmuebles['Habitaciones'].mean()#valor medio de habitaciones
print(mediaHabitaciones)
#Ahora vamos con la cantidad de baños
print("-------------Banhios--------------")
medianaBanhios = inmuebles['Banhios'].median() #mediana de Banhios
print(medianaBanhios)
minimoBanhios = inmuebles['Banhios'].min()#valor minimo de Banhios
print(minimoBanhios)
maximoBanhios = inmuebles['Banhios'].max()#valor maximo de Banhios
print(maximoBanhios)
mediaBanhios=inmuebles['Banhios'].mean()#valor medio de Banhios
print(mediaBanhios)
#Por ultimo el área de los inmuebles
print("-------------Area--------------")
medianaArea = inmuebles['Area'].median() #mediana de Area
print(medianaArea)
minimoArea = inmuebles['Area'].min()#valor minimo de Area
print(minimoArea)
maximoArea = inmuebles['Area'].max()#valor maximo de Area
print(maximoArea)
mediaArea=inmuebles['Area'].mean()#valor medio de Area
print(mediaArea)