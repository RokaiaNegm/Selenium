import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up WebDriver
driver = webdriver.Chrome()
driver.get("https://www.amazon.com/")
time.sleep(2)

# Search for a product
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("laptop")
search_box.send_keys(Keys.RETURN)
time.sleep(3)

# Scrape product names and prices
products = driver.find_elements(By.CSS_SELECTOR, "span.a-size-medium")
prices = driver.find_elements(By.CSS_SELECTOR, "span.a-price-whole")

# Save data to CSV
with open("amazon_products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Price ($)"])
    for product, price in zip(products, prices):
        writer.writerow([product.text, price.text])

# Close the browser
driver.quit()
print("✅ Data saved to amazon_products.csv")
