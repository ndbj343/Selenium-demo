from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the driver
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.maximize_window()
wait = WebDriverWait(driver, 15) 

# Step 1: Open the site
driver.get("https://www.saucedemo.com/")

# Step 2: Login
username = wait.until(
    EC.presence_of_element_located((By.ID, "user-name"))
)
username.send_keys("standard_user")

password = wait.until(
    EC.presence_of_element_located((By.ID, "password"))
)
password.send_keys("secret_sauce")

login_btn = wait.until(
    EC.element_to_be_clickable((By.ID, "login-button"))
)
login_btn.click()

# Step 3: Validate we're on the Products page
assert "inventory" in driver.current_url, "Failed: Not redirected to inventory page"
print("Inventory page URL verified")
el = driver.find_element(By.XPATH, "//span[text()='Products']")
assert el.text == "Products", "Failed: Page title text mismatch"
print("Page title text is 'Products'")

# Step 4: Wait until products are visible
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))

# Step 5: Add item to cart
products = wait.until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
)

for product in products:
    name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
    if name == "Sauce Labs Backpack":
        product.find_element(By.TAG_NAME, "button").click()
        print(f"{name} added to cart.")
        break
    else:
        print("Product not found.")

# Step 6: Click the cart icon
wait.until(
    EC.element_to_be_clickable((By.ID, "shopping_cart_container"))
).click()

# Step 7: Validate cart count
badge_cart_count = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
)
assert badge_cart_count.text == "1", "Cart count incorrect"
print("Cart shows 1 item.")

# Step 8: Validate product is listed in cart
cart_item = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_name"))
)
assert cart_item.text == "Sauce Labs Backpack", "Wrong item in cart"
print("Cart contains 'Sauce Labs Backpack'")

# Step 9: Finish
driver.quit()
