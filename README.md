# Proyecto de Ciencia de Datos
### Desde cero hasta aplicacion web.

En este proyecto realice un analisis de datos sencillo, partiendo de un dataset de las ventas semanales de una heladeria. Como dije anteriormente el dataset 'ventas.xlsx' es un archivo excel de las ventas semanales el cual se actualiza cada domingo al terminar la semana, las medidas se encuentan en kilogramos, inicalmente sus columnas eran las fechas y su fila los sabores.

  El primer problema que surgio fue la disposicion del archivo .xlsx, se encontraba en un formato dificl de extraer y utilizar los datos:
  ![image](https://user-images.githubusercontent.com/70445613/222978117-93158d8a-c274-47f6-9770-94cc3b7a7cf4.png)

  Luego de procesar el dataframe logre crear un dataframe con un formato mas adecudado, en el cual cada fila es una fecha y sus columnas son lo sabores.
  
  
  ![image](https://user-images.githubusercontent.com/70445613/222978139-fab68d50-a659-4e48-a530-cbdf3a951792.png)

Despues utilice la funcion describe() para ver un resumen rapido de los datos y me di cuenta que algunos gustos contaban con desviaciones y medias demasiado altas, por ejemplo la columna 'ANANA' tenia una venta media de 131kg lo cual es imposible realizar semanalmente. 
![image](https://user-images.githubusercontent.com/70445613/222978162-6590dba0-f8d3-4b2d-aebb-1051dec37bf5.png)

Decidi realizar un histograma para ver como estaban distribuidos los datos y descubri que habia algunso datos particularmente grandes:
  ![image](https://user-images.githubusercontent.com/70445613/222977673-6841fe6f-c68e-453c-8103-26e314a64813.png)
Revisando un poco mas el excel me di cuenta que erra un error durante la carga de datos por parte de los empleados al confundir comas y puntos, por ejemplo 9000kg de helado, signfica que se vendieron 9Kg, entonce dividi numeros >50 por 100 y mayores a 1000 por 100.
Luego de esto la disstribucion: 
![image](https://user-images.githubusercontent.com/70445613/222977782-417262a4-c885-43e9-8078-a4c2d529c0e4.png)

Despues genere una archivo func.ipynb en el cual cuenta con las funciones de agrupamiento y ordenamiento de datos, realice un analisis historico de los datos, es decir los agrupe por mes, y cree dos dataframes, uno es el dataframe agrupado por mes(ventas totales de cada columna por mes) y el segundo es la suma de las ventas totales. Ademas, partiendo del datafarme  creado, llamado: 'VentasTabla.xlsx' genere visualizciones de las ventas ordenas de manera descendente(mas vendios a menos).

Para terminar con el proeycto genere atravez de la libreria 'Streamlit' una aplicacion web,  para poder facilitar la visualizacion de los resultados para personas sin conocimientos de programacion. Todos los archivos de la aplicacion de encuentran en la carpeta Apliacion o https://github.com/fowardelcac/Projecto_Heladeria/tree/main/Aplicacion
