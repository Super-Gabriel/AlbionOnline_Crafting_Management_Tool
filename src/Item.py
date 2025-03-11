# archivo para implementar la clase item
class Item:
    def __init__(self):
        self.alias: str
        self.item_id: str
        self.item_qty: int
        self.rsrc: dict
    
    # Definir el nombre del objeto
    def set_alias(self, alias: str):
        self.alias = alias

     # Definir el ID del objeto
    def set_item_id(self, item_id: str):
        self.item_id = item_id
    
     # Definir la cantidad a craftear del objeto
    def set_item_qty(self, item_qty: int):
        self.item_qty = item_qty
    
     # Definir los recursos 
    def set_rsrc(self, rsrc: dict):
        self.rsrc = rsrc
    
    # - - - - - - - - - - - - - - - - - - - - - - - - 
    
    # Devuelve los datos para su uso en las demás clases

    def get_alias(self):
        return self.alias

    def get_item_id(self):
        return self.item_id

    def get_item_qty(self):
        return self.item_qty

    def get_rsrc(self):
        return self.rsrc

    # - - - - - - - - - - - - - - - - - - - - - - - - 

    def get_dict_format(self, dict: dict):
        format = ""
        for clave, valor in dict.items():
            format += f"{clave} : {valor}\n"
        return format
            
    def __str__(self):
        return f"Objeto: {self.alias} (ID: {self.item_id})\nCantidad: {self.item_qty}\nRecursos: \n{self.get_dict_format(self.rsrc)}"