import requests
import pandas as pd

class ApiConnection:
    def __init__(self):
        self.url: str
        self.df = pd.DataFrame(columns=["id", "city", "quality", "s_p_min", "s_p_max"])

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

        self.save_data_request(datos)

        return datos
    
    # metodo para imprimir una lista de dicts
    def save_data_request(self, list):
        for item in list:
            self.insert_row(item)

    # Metodo para imprimir un diccionario en bonito
    def insert_row(self, dct: dict):
        new_row = [dct["item_id"],dct["city"], dct["quality"], dct["sell_price_min"], dct["sell_price_max"]]
        self.df.loc[len(self.df)] = new_row

    ## setters______________________________________________________________________________________________

    def set_url(self, id: str, cities: str, quality: int):
        self.url = f"https://west.albion-online-data.com/api/v2/stats/prices/{id}?locations={cities},&qualities={quality}"


    ## getters______________________________________________________________________________________________

    def get_df_log(self):
        return self.df