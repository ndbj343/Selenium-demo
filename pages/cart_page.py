from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.item_name = (By.CLASS_NAME, "inventory_item_name")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def verify_item_in_cart(self, expected_item):
        cart_item = self.wait.until(EC.presence_of_element_located(self.item_name))
        assert cart_item.text == expected_item, "Wrong item in cart"
        print(f"Cart contains '{expected_item}'")

    def verify_cart_count(self, expected_count):
        badge_cart_count = self.wait.until(EC.visibility_of_element_located(self.cart_badge))
        assert badge_cart_count.text == expected_count, "Cart count incorrect."
        print(f"Cart shows {expected_count} item.")