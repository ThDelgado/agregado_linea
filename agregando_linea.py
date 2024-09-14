import time
import csv

class Nota:  
    def __init__(self,  texto):
        self.texto = texto


    def guardar(self):
        archivo = "notas.csv" 
        print(f"Guardando datos en {archivo}")
        try:
            with open (archivo, "a",  newline="\n") as documento: 
                writer = csv.writer(documento, delimiter=";") 

                writer.writerow([self.texto])
                time.sleep(2)
                print(f"Nota guardada correctamente en: {archivo}")
      
        except FileNotFoundError: 
            print(f"No se encuentra el archivo {archivo}") 
        except Exception as error: 
            print('Se ha generado un error no previsto', type(error).__name__)  



texto1 = Nota("Hola Mundo" ) 
texto2 = Nota("Este en una nueva línea en el archivo" )
texto3 = Nota("agregando la segunda línea del archivo" )
texto4 = Nota("finalizando la línea agregada")
    

       
texto1.guardar()
texto2.guardar()
texto3.guardar()
texto4.guardar()
