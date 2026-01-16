#pages/home_page.py

class HomePage:
    def __init__(self,page):
        self.page = page
        self.filter = ".product_sort_container"
        self.product_cart = ".shopping_cart_link"
        self.a_to_z_option = ('select[class = product_sort_container]', 'az')
        self.z_to_a_option = ('select[class = product_sort_container]', 'za')
        self.low_to_high_option = ('select[class = product_sort_container]', 'lohi')
        self.high_to_low_option = ('select[class = product_sort_container]', 'hilo')
        self.add_to_cart_button = 'button[id = "add-to-cart-{}"]'
        self.remove_from_cart_button = 'button[id = "remove-{}"]'
        self.shopping_cart = ".shopping_cart_link"