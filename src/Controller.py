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

    def main_algorithm(self):
        buy_rsrc = 60
        avg_p_rsrc = self.get_avg_price("T5_METALBAR_LEVEL1@1")

        rsrc_expense = self.calc_mng.get_expense(buy_rsrc, avg_p_rsrc)
        print(f"Precio por los recursos: {rsrc_expense}")

        # ----------------------------------------------------------------
        
        buy_obj = 30
        avg_p_obj = self.get_avg_price("T5_MAIN_AXE@1")

        obj_earnings = self.calc_mng.get_expense(buy_obj, avg_p_obj)
        print(f"Precio por los objetos: {obj_earnings}")

        # ----------------------------------------------------------------
        
        total_profit = self.calc_mng.get_profit(rsrc_expense, obj_earnings)
        print(f"Profit al craftear: {total_profit}")
        

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
