import pytest
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_login(self):
        login = LoginPage(self.driver, self.wait)
        inventory = InventoryPage(self.driver, self.wait)
        cart = CartPage(self.driver, self.wait)

        """Page 1 — Login Page """
        # Login using credentials provided
        login.login("standard_user", "secret_sauce")

        """Page 2 — Inventory Page"""
        # Validate we're on the Products page
        inventory.validate_on_inventory_page()
        assert inventory.add_to_cart("Sauce Labs Backpack"), "Product not found."
        inventory.go_to_cart()

        """Page 3 — Cart Page"""
        cart.verify_cart_count("1")
        cart.verify_item_in_cart("Sauce Labs Backpack")





