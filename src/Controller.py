from .ApiConnection import ApiConnection
from .Calculation import Calculation
from .Item import Item

class Controller:
    def __init__(self):
        self.calc_mng = Calculation()
        self.api_mng = ApiConnection()
        self.item_list: list[Item]
        self.cities: str
        self.quality: int

    # metodo para obtener el precio promedio dado el id de un objeto
    def get_avg_price(self, obj_id: str) -> float:
        lista = []
        resultado = self.api_mng.send_request(obj_id, self.cities, self.quality)
        for item in resultado:
            min_price = item.get("sell_price_min")
            max_price = item.get("sell_price_max")
            lista.append(min_price)
            lista.append(max_price)        
        #print(lista)
        lista = self.calc_mng.substract_min(lista)
        lista = self.calc_mng.substract_max(lista)
        #print(lista)
        promedio = self.calc_mng.get_promedio(lista)
        #print(promedio)
        return promedio


    ## setters _______________________________________________________________________
    def set_item_list(self, item_list: list):
        self.item_list = item_list
    def set_cities(self, cities: str):
        self.cities = cities
    def set_quality(self, quality: int):
        self.quality = quality
