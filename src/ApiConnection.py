import requests

class ApiConnection:
    def __init__(self):
        self.url: str

    # metodo para mandar una solicitud a un api
    def send_request_1(self, url: str): 
        print("enviando solicitud")
        print(url)
        

    # metodo para hacer una request dado un id, ciudades y calidad, regresa un dict con la respuesta de la api
    def send_request(self, id: str, cities: str, quality: int) -> dict[dict]:
        datos = None
        self.set_url(id, cities, quality) # seteando el url
        try:
            respuesta = requests.get(self.url) #solicitud GET
            respuesta.raise_for_status() # verificando solicitud
            datos = respuesta.json()  # convirtiendo la respuesta en dict, (como formato json)
            reversed(datos) # invirtiendo datos
        except Exception as e:
            print(f"ocurrió un error al hacer la solicitud :c {e}")
        return datos

    ## setters______________________________________________________________________________________________

    def set_url(self, id: str, cities: str, quality: int):
        self.url = f"https://west.albion-online-data.com/api/v2/stats/prices/{id}?locations={cities},&qualities={quality}"