import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\Users\\Lubna\\workspace_python\\drivers\\chromedriver.exe")
time.sleep(5)
driver.get("https://www.netflix.com/bd/")
login = driver.find_element_by_xpath("//a[@class='authLinks redButton']")
login.click()
element = driver.find_element_by_xpath("//input[@data-uia='login-field']")
element.send_keys("test1@gmail.com")

element2 = driver.find_element_by_xpath("//input[@type='password']")
element2.send_keys("test1")
submit2 = driver.find_element_by_xpath("//button[@type='submit']")
submit2.click()
time.sleep(10)
driver.quit()