import requests

class ApiConnection:

    # metodo para mandar una solicitud a un api
    def send_request(self, url: str): 
        print("enviando solicitud")
        print(url)
        try:
            # Hacer la solicitud GET
            respuesta = requests.get(url)
            
            # Verificar si la solicitud fue exitosa (código 200)
            respuesta.raise_for_status()
            
            # Convertir la respuesta a lista de diccionarios (JSON)
            datos = respuesta.json()  # Esto será una lista de objetos (diccionarios)
        
            # Procesar los datos
            for item in reversed(datos):
                # Acceder a las propiedades de cada objeto JSON
                return datos
                
        except requests.exceptions.HTTPError as errh:
            print(f"Error HTTP: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error de conexión: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Error general: {err}")
