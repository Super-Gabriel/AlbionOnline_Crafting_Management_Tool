# archivo para implementar la clase item
class Item:
    def __init__(self):
        self.alias = ""
        self.item_id = ""
        self.item_qty = 0
        self.rsrc = {}
    
    # Definir el nombre del objeto
    def set_alias(self, alias):
        self.alias = alias

     # Definir el ID del objeto
    def set_item_id(self, item_id):
        self.item_id = item_id
    
     # Definir la cantidad a craftear del objeto
    def set_item_qty(self, item_qty):
        self.item_qty = item_qty
    
     # Definir los recursos 
    def set_rsrc(self, rsrc):
        self.rsrc = rsrc
    
    # - - - - - - - - - - - - - - - - - - - - - - - - 
    
    def get_alias(self):
        return self.alias

    def get_item_id(self):
        return self.item_id

    def get_item_qty(self):
        return self.item_qty

    def get_rsrc(self):
        return self.rsrc