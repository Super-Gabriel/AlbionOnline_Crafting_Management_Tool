# archivo para implementar la clase item
class Item:
    def __init__(self):
        self.alias = ""
        self.item_id = ""
        self.item_qty = 0
        self.rsrc = {}
    
    # Definir el nombre del objeto
    def setAlias(self, alias):
        self.alias = alias

     # Definir el ID del objeto
    def setItem_id(self, item_id):
        self.item_id = item_id
    
     # Definir la cantidad a craftear del objeto
    def setItem_qty(self, item_qty):
        self.item_qty = item_qty
    
     # Definir los recursos 
    def setRsrc(self, rsrc):
        self.rsrc = rsrc
    
    # - - - - - - - - - - - - - - - - - - - - - - - - 
    
    def getAlias(self):
        return self.alias

    def getItem_id(self):
        return self.item_id

    def getItem_qty(self):
        return self.item_qty

    def getRsrc(self):
        return self.rsrc