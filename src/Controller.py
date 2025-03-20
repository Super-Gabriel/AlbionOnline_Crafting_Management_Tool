from .ApiConnection import ApiConnection
from .Calculation import Calculation
from .Item import Item
import pandas as pd
from .ControllerUtils import Utils

class Controller:
    def __init__(self):
        self.calc_mng = Calculation()
        self.api_mng = ApiConnection()
        self.utils = Utils()
        self.item_list: list[Item]
        self.cities: str
        self.quality: int
        self.p: float
        self.logs = []

    def main_algorithm(self):
        for item in self.item_list:
            item_alias = item.get_alias()
            item_id = item.get_item_id()
            item_qty = item.get_item_qty()
            item_rsrc = item.get_rsrc()
            self.calculate_profit(item_alias, item_id, item_qty, item_rsrc)
        
        #df_log = self.api_mng.get_df_log()

    # metodo para calcular el profit de un item especifico
    def calculate_profit(self, item_alias: str, item_id: str, qty: int, rsrc: dict) -> float:
        rsrc_buy_cities = []

        total_rsrc = []
        for rsrc_values in rsrc.values(): # construyendo la lista de recursos a comprar de los respectivos rsrc
            total_rsrc.append(self.calc_mng.calculate_rsrc(qty, rsrc_values, self.p))

        avg_rsrc_prices = []
        for rsrc_id in rsrc.keys(): # construyendo la lista de precios promedio de los 
            rsrc_general_list = self.utils.get_price_city_list(rsrc_id, self.cities, self.quality) # 
            rsrc_price_list = rsrc_general_list[0] # primera lista (precios)
            rsrc_city_list = rsrc_general_list[1] # segunda lista (ciudades)
            rsrc_buy_cities.append(self.utils.get_optimal_city(rsrc_price_list, rsrc_city_list)) # lista de [precios, ciudades] optimas de rsrc
            avg_rsrc_prices.append(self.utils.get_avg_price(rsrc_price_list))

        expense_list = [ x * y for x, y in zip(total_rsrc, avg_rsrc_prices)] 
        total_expenses = sum(expense_list)

        #__________________________________________________________________________________
        item_general_list = self.utils.get_price_city_list(item_id, self.cities, self.quality)
        item_price_list = item_general_list[0]
        item_city_list = item_general_list[1]
        item_sell_city = self.utils.get_worst_city(item_price_list, item_city_list) # [precio, ciudad] optima de item

        item_price = self.utils.get_avg_price(item_price_list)
        earnings = item_price * qty
        profit = earnings - total_expenses

        rsrc_ids = self.utils.get_dict_keys(rsrc)
        # construyendo y guardando el log_dict
        log_dict = self.utils.build_log_dict(item_alias, item_id, qty, item_price, item_sell_city, rsrc_ids, total_rsrc, avg_rsrc_prices, rsrc_buy_cities, total_expenses, earnings, profit)
        self.logs.append(log_dict)
        
        return profit
    
    def show_log_dicts(self):
        self.utils.show_log_dicts(self.logs)

    ## setters _______________________________________________________________________
    def set_item_list(self, item_list: list):
        self.item_list = item_list
    def set_cities(self, cities: str):
        self.cities = cities
    def set_quality(self, quality: int):
        self.quality = quality
    def set_p(self, p: float):
        self.p = p
    def set_logs(self, logs: list):
        self.logs = logs
