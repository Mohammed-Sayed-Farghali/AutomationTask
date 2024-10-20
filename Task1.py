from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize Chrome driver
driver = webdriver.Chrome()

# E-commerce App Tests
driver.get("https://e-commerce-kib.netlify.app")

try:
    # Add a new product    //*[@id="root"]/div/main/div/div/div/div[2]/div[1]/div[4]/div[2]/button[1]
    add_product_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/header/div[2]/div/a"))
    )
    add_product_button.click()

    product_name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/main/div/form/div[2]/div[1]/input"))
    )
    product_name="Test Product Automation"
    product_name_input.send_keys(product_name)

    product_price_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/main/div/form/div[3]/div/input"))
    )
    product_price_input.send_keys("10000000")
    
    product_Des = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/main/div/form/div[2]/div[2]/input"))
    )
    product_Des.send_keys("Test Product Description for Automation using selenium")
    
    
    save_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/main/div/form/button"))
    )
    save_button.click()
        

    # Verify product is added
    product_element = WebDriverWait(driver, 50).until( 
        EC.visibility_of_element_located((By.XPATH, "//*[@class='sc-jXbUNg eZFFTp flex flex-col p-4']"))
    )
    
    assert product_element.is_displayed(), "Product element not visible"
    print("Product added successfully")


    # Edit the product
    edit_Reads = driver.find_elements(By.XPATH, "//button[@class='sc-eldPxv fKKQku flex flex-col p-4']") 
    for edit_button_Read in edit_Reads:
        print(edit_button_Read.text())
        if(edit_button_Read.text()==product_name):
            edit_button = driver.find_element(By.XPATH, "//button[@class='sc-feUZmu iClHVa flex justify-center items-center h-9 w-9 transition ease-in-out delay-150 duration-300']")
            edit_button.click()    
    

    product_name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "productName"))
    )
    product_name_input.clear()
    product_name_input.send_keys("Updated Product")

    save_button = driver.find_element(By.XPATH, "//button[text()='Save']")
    save_button.click()

    # Verify product is edited
    
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[text()='Updated Product']"))
    )
    print("Product edited successfully")

    # Delete the product
    delete_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()='Updated Product']/parent::div//button[text()='Delete']"))
    )
    delete_button.click()

    # Verify product is deleted
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.XPATH, "//p[text()='Updated Product']"))
    )
    print("Product deleted successfully")

    # Search for a product
    search_input = driver.find_element(By.ID, "searchInput")
    search_input.send_keys("Product")

    # Verify search results
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Product')]"))
    )
    print("Search results found")

    # Search with multiple results
    search_input.clear()
    search_input.send_keys("Test")

    # Verify multiple search results
    search_results = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.XPATH, "//p[contains(text(),'Test')]"))
    )
    assert len(search_results) > 1, "Multiple search results not found"
    print("Multiple search results found")
    input("Waiting until enter any key")

finally:
    driver.quit()

