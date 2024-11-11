from selenium import webdriver 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = "C:/Users/akolhe/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"  # Replace with your driver's path

service = Service(executable_path=driver_path)


downloadFilepath = r"C:\Users\akolhe\Documents\HazardHub\One_way_communities\tiger-roads-automate\data\\"; 
chrome_options = webdriver.ChromeOptions() 
prefs = {"download.default_directory" : downloadFilepath} 
chrome_options.add_experimental_option('prefs', prefs) 
driver=webdriver.Chrome(service=service, options=chrome_options)




driver.get('https://www.census.gov/cgi-bin/geo/shapefiles/index.php?year=2021&layergroup=Roads')  

# driver.implicitly_wait(3)

# dropdown_state = Select(driver.find_element("id", "fips_95"))
# time.sleep(1)

# dropdown_state.select_by_visible_text('Indiana')
# time.sleep(2)

# dropdown_county = Select(driver.find_element("id", "fips__95"))
time.sleep(5)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'fips_95')))
dropdown_state = Select(driver.find_element(By.ID, 'fips_95'))
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



# for option in dropdown_county.options[1:]:
#     option_text = option.text
#     print(f'Selecting option: {option_text}')

#     dropdown_county.select_by_visible_text(option_text)
#     time.sleep(3)

#     driver.find_element(By.XPATH, '//*[@id="div_95"]/input').click()
#     time.sleep(6)





time.sleep(5)  # Adjust or add explicit wait for a specific condition

driver.quit()

print(count)
