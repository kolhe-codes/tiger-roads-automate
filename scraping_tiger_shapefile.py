from selenium import webdriver 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Replace with your driver's path (.exe path)
driver_path = r"C:\Users\......" 

service = Service(executable_path=driver_path)

# Replace with the path of the folder where you need to store the shapefiles
downloadFilepath = r"C:\Users\......\\"; 

chrome_options = webdriver.ChromeOptions() 
prefs = {"download.default_directory" : downloadFilepath} 
chrome_options.add_experimental_option('prefs', prefs) 
driver=webdriver.Chrome(service=service, options=chrome_options)


driver.get('https://www.census.gov/cgi-bin/geo/shapefiles/index.php?year=2021&layergroup=Roads')  
time.sleep(5)


WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'fips_95')))
dropdown_state = Select(driver.find_element(By.ID, 'fips_95'))
# Change the name of the state for whose counties you need the shapefiles for
dropdown_state.select_by_visible_text('North Dakota')
time.sleep(2)


WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'fips__95')))
dropdown_county = Select(driver.find_element(By.ID, 'fips__95'))
time.sleep(3)
count = 0


for option in dropdown_county.options[1:]:
    option_value = option.get_attribute('value')
    print(f'Selecting option with value: {option_value}')

    dropdown_county.select_by_value(option_value)
    time.sleep(23)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="div_95"]/input'))).click()
    time.sleep(7)
    count+=1



time.sleep(5)  
driver.quit()

print(count)
