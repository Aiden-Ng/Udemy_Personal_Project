from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time as ts


# options for element 
#methods 
    # 1. click()
    # 2. submit()
    # 3. get_attribute()
    # 4. is_selected()
    # 5. tag_name
    # 6. location
    # 7. text



def get_driver():
    #set options
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start_maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://loginfs.ntu.edu.sg/adfs/ls/?wtrealm=https%3a%2f%2fvenus2.wis.ntu.edu.sg%2fADFSSSO2%2fUser%2fLogin.aspx%2f&wctx=WsFedOwinState%3dfYGzAYcdUAB3549xxwiwZUuSEh8pqJX7RBjKQD-qa82ZKNKNcEhnCrX0dpuTrF0QR1L5AIR_SxZG_13salS0GdQ2L658lGTWsEPRTgtrIzcjj9jtyablAXdRsZigVzYwSQVcGou3Q6g9lx95U4defyq5EZE7xu4TTHM6OLlhGTbstEqHgQ3uv2bMzQVQuynIlQdxFtId9Ts-vbWbxQpeq93PGk5hAsNu1oMIQJbjUu2ffpUB3EgJNiPhOHkn1n2t&wa=wsignin1.0")
    return driver

def courtTime(driver=None, string=None):
    wait = WebDriverWait(driver, 2)  # Create an instance of WebDriverWait
    if string == "8-9":
        #Trying to achieve backward if cannot book the first court
        for i in range(2, 8):
            try:
                driver.find_element(by = "xpath", value ="/html/body/div[3]/div/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/ul/li[4]/table[2]/tbody/tr[1]/td/input").click()
                driver.find_element(by="xpath", value="/html/body/div[3]/div/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/table[2]/tbody/tr[" + str(i) + "]/td[10]/input")
                wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/input[18]")))
            except TimeoutException:
                driver.back()
    elif string_arg == "9-10":
        for i in range (8, 14):
            try:
                driver.find_element(by = "xpath", value ="/html/body/div[3]/div/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/ul/li[4]/table[2]/tbody/tr[1]/td/input").click()
                driver.find_element(by="xpath", value="/html/body/div[3]/div/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/table[2]/tbody/tr[" + str(i) + "]/td[9]/input")
                wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/input[18]")))
            except TimeoutException:
                driver.back()
    elif string_arg == "10-11":
        for i in range (14, 20):
            try:
                driver.find_element(by="xpath", value="/html/body/div[3]/div/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/table[2]/tbody/tr[" + str(i) + "]/td[9]/input")
                wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/input[18]")))
            except TimeoutException:
                driver.back()
    elif string_arg == "11-12":
        for i in range (20, 26):
            driver.find_element(by = "xpath", value = "/html/body/div[3]/div/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/table[2]/tbody/tr["+ str(i) + "]/td[9]/input")
            status = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/input[18]")))
    elif string_arg == "12-13":
        for i in range (26, 32):
            driver.find_element(by = "xpath", value = "/html/body/div[3]/div/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/table[2]/tbody/tr["+ str(i) + "]/td[9]/input")
            status = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/input[18]")))
    elif string_arg == "14-15":
        for i in range (32, 38):
            driver.find_element(by = "xpath", value = "/html/body/div[3]/div/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/table[2]/tbody/tr["+ str(i) + "]/td[9]/input")
            status = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/input[18]")))
    else:
        return 
    
def main():
    
    driver = get_driver()
    
    driver.find_element(by = "id", value = "userNameInput").send_keys("ng0004xi@student")
    driver.find_element(by = "id", value = "passwordInput").send_keys("Roboticeng911$"+ Keys.RETURN)
    ts.sleep(2)
    driver.find_element(by = "xpath", value ="/html/body/div[3]/div/div/section[2]/div/div/p/table/tbody/tr/td[1]/div/div/div[2]/div[3]/div[1]/a").click()
    ts.sleep(2)
    #driver.find_element(by = "xpath", value ="/html/body/div[3]/div/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/ul/li[4]/table[2]/tbody/tr[1]/td/input").click()
    courtTime( driver = driver, string = string_arg)
    driver.find_element( id ="xpath", value ="/html/body/div[3]/div/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/input[18]").click()

    #tr = row, td = column
    #return element.text
        
#choose your preferred timings
string_arg = "9-10"      
main()
