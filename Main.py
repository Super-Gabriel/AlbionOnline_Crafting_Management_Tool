from src.Controller import Controller
from src.Item import Item
import ItemData as idata

items = idata.items
cities = idata.cities
quality = idata.quality
p = idata.p

if __name__ == "__main__":
    
    driver = Controller()

    driver.set_item_list(items)
    driver.set_cities(cities)
    driver.set_quality(quality)
    driver.set_p(p)
    
    driver.main_algorithm()

