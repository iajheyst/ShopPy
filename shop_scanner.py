from selenium import webdriver

# import geckodriver_autoinstaller


# geckodriver_autoinstaller.install()  # Check if the current version of geckodriver exists
# and if it doesn't exist, download it automatically,
# then add geckodriver to path
import shop
from pickle_library import save_object
from produs import Produs


def parse_price(price):
    formated_price: str = price[0:len(price) - 4]
    if "de la" in formated_price:
        formated_price = formated_price[6:]
    formated_price = formated_price.replace(".", "")
    formated_price = f"{formated_price[0:-2]}.{formated_price[-2:]}"
    return float(formated_price)


driver = webdriver.Chrome()
driver.get("https://www.emag.ro/laptopuri/c?tree_ref=2172")


product_containers = driver.find_elements_by_class_name("card-section-wrapper")
print(len(product_containers))
products = []
shop = shop.Shop()
shop.delete_all_products()
for product_container in product_containers:
    title_container = product_container.find_element_by_class_name("product-title")
    title = title_container.text
    price = product_container.find_element_by_class_name("product-new-price").text
    link = title_container.get_attribute("href")
    formated_price = parse_price(price)
    product = Produs(title, formated_price, link)
    shop.add_product(product)
    # products.append(product)
    # print(link)
    # print(title)

# save_object("produse.pickle", products)
driver.close()
