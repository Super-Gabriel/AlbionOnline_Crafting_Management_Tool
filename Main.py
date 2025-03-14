from src.Controller import Controller
from src.Item import Item

cities = ",".join([
    "Martlock",
    "Thetford",
    "Fort%20Sterling",
    "Lymhurst",
    "Bridgewatch",
    "Brecilien"
])

quality = 0
p = 0.248

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
i2.set_item_qty(500)
i2_dict = {
    "T5_PLANKS_LEVEL1@1" : 8,
    "T5_METALBAR_LEVEL1@1" : 16,
}
i2.set_rsrc(i2_dict)


if __name__ == "__main__":
    
    driver = Controller()

    driver.set_item_list([i1,i2])
    driver.set_cities(cities)
    driver.set_quality(quality)
    driver.set_p(p)
    
    driver.main_algorithm()

