from src.Controller import Controller
from src.Item import Item
import ItemData as idata

items = idata.items
cities = idata.cities
quality = idata.quality
p = idata.p

driver = Controller()
driver.set_item_list(items)
driver.set_cities(cities)
driver.set_quality(quality)
driver.set_p(p)

class Menu:
    def run(self):
        input = -1
        while input!=0:
            print("_____________Menu____________\n")
            print("1. actualizar requests")
            print("2. mostrar log_dicts")
            print("0. salir\n")
            input = self.leer_int()
            self.ejecutar_opcion(input)

    def ejecutar_opcion(self, input: int):
        if input==1:
            driver.set_logs([])
            driver.main_algorithm()
        elif input==2:
            driver.show_log_dicts()
        elif input==0:
            print("adiós")
        else:
            print("opción invalida")

    def leer_int(self) -> int:
        result = -1
        try:
            result = int(input('>> '))
        except Exception as e:
            print('error al leer input')
        return result

if __name__ == "__main__":

    Menu().run()

