
class Calculation:
    def __init__(self):
        pass

    def get_promedio(self, lista: list) -> float:
        if lista:
            return sum(lista) / len(lista)
        return 0
    
    
    # metodo para substraer valores minimos innecesarios de una lista de precios
    def substract_min(self, lista: list) -> list:
        result = list(lista)
        if result:
            min_e = min(result) # primer elemento minimo
            #print(f"primer minimo: {min_e}\n verificando con lista: {lista}")
            while(self.verify_substract_min(min_e,result)):
                #print("se saca!")
                result.remove(min_e)# removiendo el elemento minimo
                if not result:
                    break
                min_e = min(result)# nuevo elemento minimo
                #print(f"siguiente minimo: {min_e}\n veficando con lista: {lista}")
            
        return result
    # metodo auxiliar para verificar si se saca o no un valor minimo
    def verify_substract_min(self, min_elem: float, lista: list) -> bool:
        result = True
        contador_true = 0
        contador_false = 0
        if(min_elem!=0):
            for item in lista:
                div = item / min_elem
                #print(f"\ndivisión de {item} / {min_elem} = {div}")
                if(div>3):
                    #print("sacalo!")
                    contador_true += 1
                else:
                    #print("no lo saques!")
                    contador_false += 1
            if contador_false > contador_true:
                result = False
        
        return result


    # metodo para substraer valores maximos innecesarios de una lista de precios
    def substract_max(self, lista: list) -> list:
        result = list(lista)
        if result:
            max_e = max(result) # primer elemento minimo
            while(self.verify_substract_max(max_e,result)):
                result.remove(max_e)# removiendo el elemento minimo
                if not result:
                    break
                max_e = max(result)# nuevo elemento 
        return result
    # metodo auxiliar para verificar si se saca o no un valor máximo
    def verify_substract_max(self, max_elem: float, lista: list) -> bool:
        result = True
        contador_true = 0
        contador_false = 0
        
        for item in lista:
            if item != 0:
                div = max_elem / item
                #print(f"\ndivisión de {item} / {min_elem} = {div}")
                if(div>3):
                    #print("sacalo!")
                    contador_true += 1
                else:
                    #print("no lo saques!")
                    contador_false += 1
        if contador_false > contador_true:
            result = False
    
        return result
    
    # Método para calcular la cantidad de recursos tomando en cuenta el porcentaje de devolución p
    def calculate_rsrc(self, n_objects: int, rsrc_qty: int, p: float) -> float:
        result = n_objects * rsrc_qty
        if rsrc_qty > 2:
            magic_v = rsrc_qty - (rsrc_qty * p)
            result = n_objects * magic_v
        return result

    # Método que devuelve los gastos al comprar cierta cantidad de recursos
    def get_expense(self, rsrc_qty: float, avg_p: float) -> float:
        return rsrc_qty * avg_p
    
    # Método que devuelve el profit total restando los gastos de la ganancia
    def get_profit(self, expenses: float, earnings: float) -> float:
        return earnings - expenses