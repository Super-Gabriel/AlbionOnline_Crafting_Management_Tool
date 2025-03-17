from src.Item import Item
import copy
items = []
quality = 0
p = 0.24
cities = ",".join([
    "Martlock",
    "Thetford",
    "Fort%20Sterling",
    "Lymhurst",
    "Bridgewatch",
    "Brecilien"
])

# items
i = Item()

# seteando info de items
i.set_alias("Invocador oscuro")
i.set_item_id("T5_MAIN_CURSEDSTAFF_AVALON@1")
i.set_item_qty(20)
i_dict = {
    "T5_PLANKS_LEVEL1@1" : 16,
    "T5_METALBAR_LEVEL1@1" : 8,
    "T5_ARTEFACT_MAIN_CURSEDSTAFF_AVALON": 1
}
i.set_rsrc(i_dict)
items.append(copy.deepcopy(i))

#___________________________________________________

i.set_alias("hacha de guerra")
i.set_item_id("T5_MAIN_AXE@1")
i.set_item_qty(20)
i_dict = {
    "T5_PLANKS_LEVEL1@1" : 8,
    "T5_METALBAR_LEVEL1@1" : 16
}
i.set_rsrc(i_dict)
items.append(copy.deepcopy(i))

#___________________________________________________

i.set_alias("Vela de Crypta 4.1")
i.set_item_id("T4_OFF_LAMP_UNDEAD@1")
i.set_item_qty(20)
i_dict = {
    "T4_PLANKS_LEVEL1@1" : 4,
    "T4_CLOTH_LEVEL1@1" : 4,
    "T4_ARTEFACT_OFF_LAMP_UNDEAD" : 1
}
i.set_rsrc(i_dict)
items.append(copy.deepcopy(i))

#___________________________________________________

i.set_alias("Vela de Crypta 5.1")
i.set_item_id("T5_OFF_LAMP_UNDEAD@1")
i.set_item_qty(20)
i_dict = {
    "T5_PLANKS_LEVEL1@1" : 4,
    "T5_CLOTH_LEVEL1@1" : 4,
    "T5_ARTEFACT_OFF_LAMP_UNDEAD" : 1
}
i.set_rsrc(i_dict)
items.append(copy.deepcopy(i))