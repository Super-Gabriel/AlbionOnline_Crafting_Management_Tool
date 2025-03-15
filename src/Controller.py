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
        self.logs = []

    def main_algorithm(self):
        profits = []
        for item in self.item_list:
            item_id = item.get_item_id()
            item_qty = item.get_item_qty()
            item_rsrc = item.get_rsrc()
            item_profit = self.calculate_profit(item_id, item_qty, item_rsrc)
            item_name = item.get_alias()
            profits.append([item_name, item_profit])

        print(self.logs)
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
        item_price = self.get_avg_price(item_id)
        earnings = item_price * qty
        profit = earnings - total_expenses

        rsrc_ids = self.get_dict_keys(rsrc)

        log_dict = self.build_log_dict(item_id, qty, item_price, rsrc_ids, total_rsrc, avg_rsrc_prices, total_expenses, earnings, profit)
        self.logs.append(log_dict)
        
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

    # Método para construir un log_dict
    def build_log_dict(self, 
                       item_id: str, 
                       qty: int, 
                       item_price: float, 
                       rsrc_ids: list, 
                       total_rsrc: list, 
                       avg_rsrc_prices: list, 
                       total_expenses: float, 
                       earnings: float, 
                       profit: float) -> dict:
        
        rsrc_info_dict = {}
        contador = 1
        for id, total_rsrc, avg_rsrc_price in zip(rsrc_ids, total_rsrc, avg_rsrc_prices):
            rsrc_info_dict[f'rsrc{contador}_name'] = id
            rsrc_info_dict[f'rsrc{contador}_qty'] = total_rsrc
            rsrc_info_dict[f'rsrc{contador}_avg_price'] = avg_rsrc_price
            contador += 1

        result = {}
        result['item_name'] = item_id
        result['item_qty'] = qty
        result['item_avg_price'] = item_price
        result['rsrc_info'] = rsrc_info_dict
        result['total_expenses'] = total_expenses
        result['earnings'] = earnings
        result['profit'] = profit
        
        return result
    
    # Método para obtener las keys de un dict
    def get_dict_keys(self, dct: dict) -> list:
        result = []
        for key in dct.keys():
            result.append(key)
        return result

    ## setters _______________________________________________________________________
    def set_item_list(self, item_list: list):
        self.item_list = item_list
    def set_cities(self, cities: str):
        self.cities = cities
    def set_quality(self, quality: int):
        self.quality = quality
    def set_p(self, p: float):
        self.p = p
