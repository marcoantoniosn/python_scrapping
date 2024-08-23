import requests
from bs4 import BeautifulSoup

url ="https://listado.mercadolibre.com.pe/zapatillas-hombre#D[A:zapatillas%20hombre]"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    productos = soup.find_all('div',class_="andes-card poly-card poly-card--grid-card andes-card--flat andes-card--padding-0 andes-card--animated")
    
    for producto in productos:
        titulo = producto.find('h2',class_="poly-box")        
        marca = producto.find('span',class_="poly-component__brand")    
        if titulo:            
            print(titulo.text.strip())
        if marca:
            print(marca.text.strip())
else:
    print("Error de pagina ,codigo:", response.status_code)    
    
    
    