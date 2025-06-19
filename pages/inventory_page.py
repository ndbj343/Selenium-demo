from openpyxl.styles.builtins import title
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage():
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.product_title = (By.XPATH, "//span[text()='Products']")
        self.items = (By.CLASS_NAME, "inventory_item")
        self.cart_icon = (By.ID, "shopping_cart_container")

    def validate_on_inventory_page(self):
        assert "inventory" in self.driver.current_url
        title =self.wait.until(EC.presence_of_element_located(self.product_title))
        assert title.text == "Products", "Incorrect page title"

    def add_to_cart(self, product_name):
        products = self.wait.until(EC.presence_of_all_elements_located(self.items))
        for product in products:
            name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
            if name == product_name:
                product.find_element(By.TAG_NAME, "button").click()
                return True

        return False

    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.cart_icon)).click()