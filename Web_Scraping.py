from selenium import webdriver

def main():
    #set options 
    print("Hello world")
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start_maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")   
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")



