from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")
logo = driver.find_element_by_xpath("//a[contains(text(), 'Continue')]")
new_registrant_btn = driver.find_element_by_xpath("//a[contains(text(), 'Continue')]")
new_registrant_btn.click()
element=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(), 'Continue')]")))