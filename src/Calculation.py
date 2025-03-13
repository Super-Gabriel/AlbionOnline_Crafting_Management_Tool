
class Calculation:
    def __init__(self):
        pass

    def get_promedio(self, lista) -> float:
        return sum(lista) / len(lista)
    
    
    # metodo para substraer valores minimos innecesarios de una lista de precios
    def substract_min(self, lista: list) -> list:
        min_e = min(lista) # primer elemento minimo
        #print(f"primer minimo: {min_e}\n verificando con lista: {lista}")
        while(self.verify_substract_min(min_e,lista)):
            #print("se saca!")
            lista.remove(min_e)# removiendo el elemento minimo
            min_e = min(lista)# nuevo elemento minimo
            #print(f"siguiente minimo: {min_e}\n veficando con lista: {lista}")
        
        return lista
    # metodo auxiliar para verificar si se saca o no un valor minimo
    def verify_substract_min(self, min_elem, lista) -> bool:
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
        max_e = max(lista) # primer elemento minimo
        while(self.verify_substract_max(max_e,lista)):
            lista.remove(max_e)# removiendo el elemento minimo
            max_e = max(lista)# nuevo elemento minimo
        return lista
    # metodo auxiliar para verificar si se saca o no un valor máximo
    def verify_substract_max(self, max_elem, lista) -> bool:
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