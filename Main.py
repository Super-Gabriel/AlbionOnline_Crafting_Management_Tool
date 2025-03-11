from src.Controller import Controller
from src.Item import Item

class Main:
    driver = Controller([])

    def init(self, item_list: list):
        self.driver = Controller(item_list)

    # metodo para leer un entero, si hay un error regresa -1
    def read_int(self) -> int:
        entrada = -1
        try:
            entrada = int(input(">> "))
        except:
            print("input invalido")

        return entrada
        

    def run_menu(self):
        input = -1
        while input != 0:
            print("\n1 - hacer request")
            print("2 - prueba actual (verificación de datos en controller)")
            print("0 - salir")
            input = self.read_int()
            self.driver.opcion(input)


if __name__ == "__main__":
    # items
    i1 = Item()
    i2 = Item()

    # seteando info de items
    i1.set_alias("Invocador oscuro")
    i1.set_item_id("T5_MAIN_CURSEDSTAFF_AVALON@1")
    i1.set_item_qty(20)
    i1_dict = {
        "T5_PLANKS_LEVEL1@1" : 16,
        "T5_METALBAR_LEVEL1@1" : 8,
        "T5_ARTEFACT_MAIN_CURSEDSTAFF_AVALON": 1
    }

    i1.set_rsrc(i1_dict)

    i2.set_alias("hacha de guerra")
    i2.set_item_id("T5_MAIN_AXE@1")
    i2.set_item_qty(20)
    i2_dict = {
        "T5_PLANKS_LEVEL1@1" : 8,
        "T5_METALBAR_LEVEL1@1" : 16,
    }
    i2.set_rsrc(i2_dict)

    # iniciando menú
    main = Main()
    main.init([i1, i2])
    main.run_menu() # corriendo el menú
    #item1 = Item()

    

