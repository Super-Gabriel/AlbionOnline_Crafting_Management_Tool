from .ApiConnection import ApiConnection

class Controller:
    api_mng = ApiConnection()

    # metodo para 
    def opcion(self, opcion):
        if opcion == 1:
            self.make_request()
        elif opcion == 0:
            print("saliendo")
        else:
            print("opción invalida")

    # metodo para hacer una request al api mediante url
    def make_request(self):
        url = "https://west.albion-online-data.com/api/v2/stats/prices/T4_BAG,T5_BAG?locations=Martlock&qualities=1"
        self.api_mng.send_request(url)

