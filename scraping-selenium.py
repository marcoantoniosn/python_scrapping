from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import pandas as pd

# Inicializar listas vacías para cada columna del Excel
lst_titulo = []
lst_empresa = []
lst_lugar = []
lst_desde = []

# Especificar el nombre del archivo y el nombre de la hoja de resultado
nombre_archivo = "datos_computrabajo.xlsx"
nombre_hoja = ["Jefe de Sistemas","Jefe de TI","Jefe de Proyectos","Coordinador de Proyectos","Gestor de Proyectos","Lider Tecnico"]

num_cargos = 7 #6 Cargos

for c in range(1, num_cargos):
    # Número de páginas que deseas recorrer
    num_pages = 5 #6 Paginas
    
    #Empezamos lecturas por cargo:
    j=0
    driver = webdriver.Chrome()                 
    url ="https://pe.computrabajo.com/trabajo-de-"+ nombre_hoja[c-1]
    
    driver.get(url)

    for i in range(num_pages):
        try:
            j=j+1
            html = driver.page_source
            soup = BeautifulSoup(html,'html.parser')
            cargos = soup.find_all('article',class_="box_offer")
            for cargo in cargos:
                titulo = cargo.find('h2',class_="fs18 fwB")                        
                empresa = cargo.find('p',class_="dIB fs16 fc_base mt5")    
                empresa_nombre1= empresa.find('a')                  
                lugar = cargo.find('p',class_="fs16 fc_base mt5")                                
                lugar1 = lugar.find('span')
                desde = cargo.find('p',class_="fs13 fc_aux mt15")                                
                if titulo:            
                    #print(titulo.text.strip().upper())
                    lst_titulo.append(titulo.text.strip().upper())
                if empresa_nombre1:
                    #print(empresa_nombre1.text.strip())
                    lst_empresa.append(empresa_nombre1.text.strip())
                else:
                    #print(empresa.text.strip())                 
                    lst_empresa.append(empresa.text.strip())
                if lugar1:
                    #print(lugar1.text.strip())   
                    lst_lugar.append(lugar1.text.strip())
                if desde:
                #print(desde.text.strip())     
                    lst_desde.append(desde.text.strip())
            
            # Ejemplo: encontrar el enlace al botón "Next"        
            next_button = driver.find_element(By.XPATH, "//span[@class='b_primary w48 buildLink cp' and @title='Siguiente']")
            next_button.click()        
            # Espera un poco para que la página cargue completamente
            time.sleep(2)         
        except Exception as e:
            print(f"Error al procesar la página {i + 1}: {e}")
            break     
                
    # Cierra el navegador
    driver.quit()       

    # Crear un DataFrame a partir de las listas
    datos = {
        "Titulo": lst_titulo,
        "Empresa": lst_empresa,
        "Lugar": lst_lugar,
        "Desde": lst_desde
    }

    if c==1:
        df1 = pd.DataFrame(datos)
        # Limpiar lista
        for key in datos:
            datos[key].clear()
    elif c==2:
        df2 = pd.DataFrame(datos)
        # Limpiar lista
        for key in datos:
            datos[key].clear()
    elif c==3:
        df3 = pd.DataFrame(datos)
        # Limpiar lista
        for key in datos:
            datos[key].clear()        
    elif c==4:
        df4 = pd.DataFrame(datos)
        # Limpiar lista
        for key in datos:
            datos[key].clear()
    elif c==5:
        df5 = pd.DataFrame(datos)
        # Limpiar lista
        for key in datos:
            datos[key].clear()            
    elif c==6:
        df6 = pd.DataFrame(datos)
        # Limpiar lista
        for key in datos:
            datos[key].clear()            
            
# Guardar los datos en un archivo Excel
#df.to_excel("datos_computrabajo.xlsx", index=False)
with pd.ExcelWriter(nombre_archivo, engine='openpyxl') as writer:
    df1.to_excel(writer, sheet_name=nombre_hoja[0], index=False)
    df2.to_excel(writer, sheet_name=nombre_hoja[1], index=False)   
    df3.to_excel(writer, sheet_name=nombre_hoja[2], index=False)   
    df4.to_excel(writer, sheet_name=nombre_hoja[3], index=False)   
    df5.to_excel(writer, sheet_name=nombre_hoja[4], index=False)
    df6.to_excel(writer, sheet_name=nombre_hoja[5], index=False)
    