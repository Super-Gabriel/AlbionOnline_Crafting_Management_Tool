from .ApiConnection import ApiConnection
from .Item import Item

class Controller:
    api_mng = ApiConnection()
    item_list: list[Item]

    # metodo constructor que recibe una lista de Item
    def __init__(self, item_list: list):
        self.item_list = item_list

    # metodo para 
    def opcion(self, opcion):
        if opcion == 1:
            self.make_request()
        elif opcion == 2:
            self.current_test()
        elif opcion == 0:
            print("saliendo")
        else:
            print("opción invalida")

    # metodo para hacer una request al api mediante url
    def make_request(self):
        url = "https://west.albion-online-data.com/api/v2/stats/prices/T4_BAG,T5_BAG?locations=Martlock&qualities=1"
        self.api_mng.send_request(url)

    #metodo para desarrollar la prueba actual
    def current_test(self):
        for x in self.item_list:            
            print(x) # ya se obtienen los datos de la lista de items C:

    # metodo para obtener el precio promedio dado el id de un objeto
    def get_avg_price(self, obj_id: str) -> float:
        pass

