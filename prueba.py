from src.Controller import Controller
from src.Item import Item

hola = Controller()

obj_1 = Item()
obj_2 = Item()

obj_1.set_alias("Invocador oscuro")
obj_1.set_item_id("T5_MAIN_CURSEDSTAFF_AVALON@1")
obj_1.set_item_qty(20)
obj_1_dict = {
    "T5_PLANKS_LEVEL1@1" : 16,
    "T5_METALBAR_LEVEL1@1" : 8,
    "T5_ARTEFACT_MAIN_CURSEDSTAFF_AVALON": 1
}

obj_1.set_rsrc(obj_1_dict)

obj_2.set_alias("hacha de guerra")
obj_2.set_item_id("T5_MAIN_AXE@1")
obj_2.set_item_qty(20)
obj_2_dict = {
    "T5_PLANKS_LEVEL1@1" : 8,
    "T5_METALBAR_LEVEL1@1" : 16,
}
obj_2.set_rsrc(obj_2_dict)

hola.set_cities("Martlock")
hola.set_quality(1)
hola.main_algorithm()