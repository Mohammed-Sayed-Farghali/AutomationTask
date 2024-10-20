from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://flutter-angular.web.app")

# Wait for the Flutter app to load
WebDriverWait(driver, 100).until(
    EC.presence_of_element_located((By.TAG_NAME, "flutter-view"))
)

# Get the flutter-view element
flutter_view = driver.find_element(By.TAG_NAME, "flutter-view")
dim = flutter_view.size
print(dim)

# Calculate approximate coordinates of the "+" button (adjust as needed)
x_offset = dim['width'] /2  # Example: 75% from the left edge
y_offset = dim['height'] /2   # Example: 50% from the top 

x=(x_offset*0.85)
y=(y_offset*0.90)

# Create an ActionChains object
actions = ActionChains(driver)

# Move to the approximate coordinates and click
actions.move_to_element_with_offset(flutter_view, x, y).click().perform()

#We can use another way using OpenCV to get the image of Flatter View and extract the exact elemnet 



#plus_button = driver.find_element(By.XPATH, "//flutter-view")
# Click the button
#plus_button.click()
input("Waiting until enter any key")