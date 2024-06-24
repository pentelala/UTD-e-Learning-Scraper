from urllib.request import urlopen
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://elearning.utdallas.edu")
# driver.get("https://idp.utdallas.edu/idp/profile/SAML2/POST/SSO?execution=e3s1")

# Finding login elements
driver.find_element(By.ID, "netid").send_keys("NetID")
driver.find_element(By.ID, "password").send_keys("Password")
driver.find_element(By.ID, "submit").click()

print(driver.current_url)



# html = urlopen('https://elearning.utdallas.edu/ultra/institution-page')
# bs = BeautifulSoup(html, 'lxml')

