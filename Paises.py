#Extraccion de datos de la url: https://es.wikipedia.org/wiki/Am%C3%A9rica
import requests
from bs4 import BeautifulSoup
import csv
import codecs

url = 'https://es.wikipedia.org/wiki/Am%C3%A9rica'

#Realizamos una solicitud GET a la url
response = requests.get(url)

#verificar si la solicitud fue exitosa (codigo de estado 200)
if response.status_code == 200:
    
    #Parsear el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    table = soup.find('table', {'class': 'wikitable'})

    #Crear un archivo CSV llamado paises.csv en modo de escritura
     #with open('paises.csv', 'w', newline='', encoding='utf-8') as csvfile:
    with codecs.open('paises2.csv', 'w', 'utf-8-sig') as csvfile:

        archivo = csv.writer(csvfile)
        
        #Escribir encabezado
        archivo.writerow(['País', 'Población', 'Fecha de Independencia', 'Capítal'])


        #iterar sobre las filas de la tabal
        for row in table.find_all('tr')[1:]:
            columns = row.find_all('td')
        
            pais = columns[2].text.strip()
            poblacion = columns[5].text.strip()
            fecha_indep = columns[3].text.strip()

            if(len(columns)>7):
                capital = columns[7].text.strip()
            else:
                capital=0

            print("Pais:",pais, "Capital:",capital,"Poblacion:",poblacion,"Independencia:",fecha_indep)
            archivo.writerow([pais,poblacion,fecha_indep,capital])

        print ("Archivo csv crear correctamente.")
        

       