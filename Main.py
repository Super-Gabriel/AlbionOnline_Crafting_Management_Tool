from src.Controller import Controller
from src.Item import Item

driver = Controller()

# metodo para leer un entero, si hay un error regresa -1
def read_int() -> int:
    entrada = -1
    try:
        entrada = int(input(">> "))
    except:
        print("input invalido")

    return entrada
    

def run_menu():
    input = -1
    while input != 0:
        print("\n1 - hacer request")
        print("0 - salir")
        input = read_int()
        driver.opcion(input)


if __name__ == "__main__":
    #run_menu() # corriendo el menú
    item1 = Item()


