from .Calculation import Calculation
from .ApiConnection import ApiConnection

class Utils:
    def __init__(self):
        self.calc_mng = Calculation()
        self.api_mng = ApiConnection()

    # metodo para obtener [precio_optimo, ciudad] dada una lista de precios y un lista de ciudades
    def get_optimal_city(self, prices: list, cities: list) -> list:
        result=[]
        prices_cleaned = self.calc_mng.substract_max(self.calc_mng.substract_min(prices))
        if prices_cleaned:
            optimal_price_index = prices.index(min(prices_cleaned))
            result = [prices[optimal_price_index], cities[optimal_price_index]]
        return result
    
    # metodo para obtener [precio_más_alto, ciudad] dada una lista de precios y una lista de ciudades
    def get_worst_city(self, prices: list, cities: list) ->list :
        result=[]
        prices_cleaned = self.calc_mng.substract_max(self.calc_mng.substract_min(prices))
        if prices_cleaned:
            optimal_price_index = prices.index(max(prices_cleaned))
            result = [prices[optimal_price_index], cities[optimal_price_index]]
        return result
    
    # metodo para obtener la lista de precios y su ciudad dado un id
    def get_price_city_list(self, obj_id: str, cities: str, quality: int) -> list:
        lista = [[],[]]
        resultado = self.api_mng.send_request(obj_id, cities, quality)
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

    # Método para construir un log_dict
    def build_log_dict(self, 
                       item_alias: str, 
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
        percent = 0
        if total_expenses != 0:
            percent = profit * (100/total_expenses)
        contador = 1
        for id, total_rsrc, avg_rsrc_price in zip(rsrc_ids, total_rsrc, avg_rsrc_prices):
            rsrc_info_dict[f'rsrc{contador}_id'] = id
            rsrc_info_dict[f'rsrc{contador}_qty'] = total_rsrc
            rsrc_info_dict[f'rsrc{contador}_avg_price'] = avg_rsrc_price
            rsrc_info_dict[f'rsrc{contador}_optimal_city'] = rsrc_buy_cities[contador-1]
            contador += 1

        result = {}
        result['item_alias'] = item_alias
        result['item_id'] = item_id
        result['item_qty'] = qty
        result['item_avg_price'] = item_price
        result['optimal_city'] = item_sell_city
        result['rsrc_info'] = rsrc_info_dict
        result['total_expenses'] = total_expenses
        result['earnings'] = earnings
        result['profit'] = profit
        result["%"] = percent

        return result
    
    # Método para obtener las keys de un dict
    def get_dict_keys(self, dct: dict) -> list:
        result = []
        for key in dct.keys():
            result.append(key)
        return result

    # metodo para mostrar los log_dicts
    def show_log_dicts(self, logs: dict):
        for i in logs:
            self.show_dict(i)
            print("\n")

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
        print()
        for clave, valor in dct.items():
            print(f"\t\t{clave} : {valor}")
            if clave.endswith("optimal_city"):
                print()