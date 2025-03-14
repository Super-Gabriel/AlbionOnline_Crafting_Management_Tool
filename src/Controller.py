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
        self.p: float

    def main_algorithm(self):
        profits = []
        for item in self.item_list:
            item_id = item.get_item_id()
            item_qty = item.get_item_qty()
            item_rsrc = item.get_rsrc()
            item_profit = self.calculate_profit(item_id, item_qty, item_rsrc)
            item_name = item.get_alias()
            profits.append([item_name, item_profit])

        print(profits)

    # metodo para calcular el profit de un item especifico
    def calculate_profit(self, item_id: str, qty: int, rsrc: dict) -> float:
        total_rsrc = []
        for rsrc_values in rsrc.values(): # construyendo la lista de recursos a comprar de los respectivos rsrc
            total_rsrc.append(self.get_total_resources(qty, rsrc_values, self.p))

        avg_rsrc_prices = []
        for rsrc_id in rsrc.keys(): # construyendo la lista de precios promedio de los recursos
            avg_rsrc_prices.append(self.get_avg_price(rsrc_id))

        expense_list = [ x * y for x, y in zip(total_rsrc, avg_rsrc_prices)]
        total_expenses = sum(expense_list)
        #__________________________________________________________________________________
        earnings = self.get_avg_price(item_id) * qty
        profit = earnings - total_expenses

        return profit

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

    # Método para calcular la cantidad de recursos tomando en cuenta el porcentaje de devolución p
    def get_total_resources(self, n_objects: int, rsrc_qty: int, p: float) -> float:
        if rsrc_qty > 1:
            return self.calc_mng.calculate_rsrc(n_objects, rsrc_qty, p)
        return n_objects


    ## setters _______________________________________________________________________
    def set_item_list(self, item_list: list):
        self.item_list = item_list
    def set_cities(self, cities: str):
        self.cities = cities
    def set_quality(self, quality: int):
        self.quality = quality
    def set_p(self, p: float):
        self.p = p
