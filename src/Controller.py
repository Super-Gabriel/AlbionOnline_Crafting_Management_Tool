from .ApiConnection import ApiConnection
from .Calculation import Calculation
from .Item import Item
import pandas as pd

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
        
        for i in range(len(self.item_list)):
            self.show_dict(self.logs[i])
            print("\n")
        
        df_log = self.api_mng.get_df_log()

        #print(self.logs)
        #print(profits)

    # metodo para calcular el profit de un item especifico
    def calculate_profit(self, item_id: str, qty: int, rsrc: dict) -> float:
        rsrc_buy_cities = []

        total_rsrc = []
        for rsrc_values in rsrc.values(): # construyendo la lista de recursos a comprar de los respectivos rsrc
            total_rsrc.append(self.get_total_resources(qty, rsrc_values, self.p))

        avg_rsrc_prices = []
        for rsrc_id in rsrc.keys(): # construyendo la lista de precios promedio de los 
            rsrc_general_list = self.get_price_city_list(rsrc_id) # 
            rsrc_price_list = rsrc_general_list[0] # primera lista (precios)
            rsrc_city_list = rsrc_general_list[1] # segunda lista (ciudades)
            rsrc_buy_cities.append(self.get_optimal_city(rsrc_price_list, rsrc_city_list)) # lista de [precios, ciudades] optimas de rsrc
            avg_rsrc_prices.append(self.get_avg_price(rsrc_price_list))

        expense_list = [ x * y for x, y in zip(total_rsrc, avg_rsrc_prices)] 
        total_expenses = sum(expense_list)

        #__________________________________________________________________________________
        item_general_list = self.get_price_city_list(item_id)
        item_price_list = item_general_list[0]
        item_city_list = item_general_list[1]
        item_sell_city = self.get_worst_city(item_price_list, item_city_list) # [precio, ciudad] optima de item

        item_price = self.get_avg_price(item_price_list)
        earnings = item_price * qty
        profit = earnings - total_expenses

        rsrc_ids = self.get_dict_keys(rsrc)
        # construyendo y guardando el log_dict
        log_dict = self.build_log_dict(item_id, qty, item_price, item_sell_city, rsrc_ids, total_rsrc, avg_rsrc_prices, rsrc_buy_cities, total_expenses, earnings, profit)
        self.logs.append(log_dict)
        
        return profit
    
    # metodo para obtener [precio_optimo, ciudad] dada una lista de precios y un lista de ciudades
    def get_optimal_city(self, prices: list, cities: list) -> list:
        result=[]
        prices_cleaned = self.calc_mng.substract_max(self.calc_mng.substract_min(prices))
        optimal_price_index = prices.index(min(prices_cleaned))
        result = [prices[optimal_price_index], cities[optimal_price_index]]
        return result

    # metodo para obtener [precio_más_alto, ciudad] dada una lista de precios y una lista de ciudades
    def get_worst_city(self, prices: list, cities: list) ->list :
        result=[]
        prices_cleaned = self.calc_mng.substract_max(self.calc_mng.substract_min(prices))
        optimal_price_index = prices.index(max(prices_cleaned))
        result = [prices[optimal_price_index], cities[optimal_price_index]]
        return result

    # metodo para obtener la lista de precios y su ciudad dado un id
    def get_price_city_list(self, obj_id: str) -> list:
        lista = [[],[]]
        resultado = self.api_mng.send_request(obj_id, self.cities, self.quality)
        for item in resultado:
            min_price = item.get("sell_price_min")
            max_price = item.get("sell_price_max")
            city = item.get("city")
            lista[0].append(min_price)
            lista[0].append(max_price)
            lista[1].append(city)
            lista[1].append(city)

        #print(f"\nid: {obj_id}")
        #self.print_two_lists(lista[0], lista[1])
        return lista
    
    def print_two_lists(self, l1: list, l2: list):
        for i1, i2 in zip(l1,l2):
            if i1!=0:
                print(f"{i1} - {i2}")
    
    def prin_two_lists_1(self, l1: list, l2: list):
        contador = 0
        for i1, i2 in zip(l1,l2):
            print(f"[{contador}] : {i1} - {i2}")
            contador +=1

    # metodo para obtener el precio promedio dada la lista de precios de un objeto
    def get_avg_price(self, lista: list) -> float:
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
                       item_sell_city: list, 
                       rsrc_ids: list, 
                       total_rsrc: list, 
                       avg_rsrc_prices: list,
                       rsrc_buy_cities: list[list], 
                       total_expenses: float, 
                       earnings: float, 
                       profit: float) -> dict:
        
        rsrc_info_dict = {}
        contador = 1
        for id, total_rsrc, avg_rsrc_price in zip(rsrc_ids, total_rsrc, avg_rsrc_prices):
            rsrc_info_dict[f'rsrc{contador}_name'] = id
            rsrc_info_dict[f'rsrc{contador}_qty'] = total_rsrc
            rsrc_info_dict[f'rsrc{contador}_avg_price'] = avg_rsrc_price
            rsrc_info_dict[f'rsrc{contador}_optimal_city'] = rsrc_buy_cities[contador-1]
            contador += 1

        result = {}
        result['item_name'] = item_id
        result['item_qty'] = qty
        result['item_avg_price'] = item_price
        result['optimal_city'] = item_sell_city
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
    
    # Metodo para imprimir un diccionario en bonito
    def show_dict(self, dct: dict):
        print("______________________________________________________________________")
        for clave, valor in dct.items():
            if type(valor) == dict:
                self.show_inside_dict(valor)
            else:
                print(f"\t{clave} : {valor}")
        print("______________________________________________________________________")

    def show_inside_dict(self, dct: dict):
        for clave, valor in dct.items():
            print(f"\t\t{clave} : {valor}")

    ## setters _______________________________________________________________________
    def set_item_list(self, item_list: list):
        self.item_list = item_list
    def set_cities(self, cities: str):
        self.cities = cities
    def set_quality(self, quality: int):
        self.quality = quality
    def set_p(self, p: float):
        self.p = p
