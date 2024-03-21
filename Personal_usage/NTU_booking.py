from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
    driver.get("https://loginfs.ntu.edu.sg/adfs/ls/?wtrealm=https%3a%2f%2fvenus2.wis.ntu.edu.sg%2fADFSSSO2%2fUser%2fLogin.aspx%2f&wctx=WsFedOwinState%3dc6nVSNGYyLgdF2wVh-glkfMh2hSZ3ZD7L0ZgOsoBfiXhH1aQPJiE1lq3BjQQJ5NS7MflphBzV75aiU44ZAStk-UE8nWdUvIkX-LAaPakn0I4KUw7pmjwN4uI_9bJTMKT3o2edLu440fCupI9_e2Km-lyi9LremqfJ3tGrpBeIdVxRpW6TYPp4wMxWBcCxOkB3UWbWDPPN80arTwrBHpz9OAkm4rYpXfq1TYuR9hbtPXxaxp6kE61giAiB_PGsNTe&wa=wsignin1.0")
    return driver

def main():
    driver = get_driver()
    driver.find_element(by = "id", value = "userNameInput").send_keys("ng0004xi@student")
    driver.find_element(by = "id", value = "passwordInput").send_keys("Roboticeng911$"+ Keys.RETURN)
    ts.sleep(2)
    driver.find_element(by = "xpath", value ="/html/body/div[3]/div/div/section[2]/div/div/p/table/tbody/tr/td[1]/div/div/div[2]/div[3]/div[1]/a").click()
    ts.sleep(2)
    driver.find_element(by = "xpath", value ="/html/body/div[3]/div/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/ul/li[4]/table[2]/tbody/tr[1]/td/input").click()
    driver.find_element(by = "xpath", value ="/html/body/div[3]/div/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/table[2]/tbody/tr[8]/td[10]/input").click()
    driver.find_element(by = "xpath", value ="/html/body/div[3]/div/div/section[2]/div/div/p/table/tbody/tr/td[2]/form/input[18]").click()

    

    #return element.text


main()


