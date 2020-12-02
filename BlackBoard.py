import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='path') 
#path

driver.get('https://learn.uark.edu/webapps/login/');
time.sleep(1)
start = time.time()
button = driver.find_element_by_id('agree_button')
button.click()

elem = driver.find_element_by_link_text("University of Arkansas Organization Login")
elem.click()
time.sleep(1)

button = driver.find_element_by_id('i0116')
button.click()


button.send_keys("user@uark.edu")
#user

button = driver.find_element_by_id('idSIButton9')
button.click()

button = driver.find_element_by_name('passwd')

button.send_keys("password")
time.sleep(1)
#password

button = driver.find_element_by_id('idSIButton9')
button.click()
time.sleep(1)

button = driver.find_element_by_id('idBtn_Back')
button.click()


driver.maximize_window()
end = time.time()
print("That took", end-start,"seconds!")
