from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
import argparse

def main(timing, court):
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://venus2.wis.ntu.edu.sg/ADFSSSO2/User/Login.aspx?app=https://wis.ntu.edu.sg/pls/webexe88/srce_smain_s.Notice_O")
    wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds for elements to become interactable

    # Open the file in read mode
    with open("login.txt", "r") as file:
        # Read the first line and store it in a variable
        username = file.readline().strip()
        print(username)
        # Read the second line and store it in another variable
        password = file.readline().strip()
        print(password)

    # Find the input field by ID and enter your username and password
    username_input = wait.until(EC.element_to_be_clickable((By.ID, 'userNameInput')))
    username_input.send_keys(username)
    password_input = wait.until(EC.element_to_be_clickable((By.ID, 'passwordInput')))
    password_input.send_keys(password)

    # Find the sign-in button by ID and click it
    sign_in_button = wait.until(EC.element_to_be_clickable((By.ID, 'submitButton')))
    sign_in_button.click()

    # Calculate the time remaining until 12 AM
    now = datetime.datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0) + datetime.timedelta(days=1)  # Next day midnight
    time_until_midnight = midnight - now
    print(time_until_midnight)

    # Wait until 12 am
    time.sleep(time_until_midnight.seconds)

    # Record the start time
    start_time = time.time()

    # Find the gym button by its attributes and click it
    #1BB2BB0218-Sep-20236
    #1BB2BB(type) 02(court) 18-Sep-2023(date) 6(slot from start of day)
    facility_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @name="p_info" and @value="1BB26"]')))
    facility_button.click()

    # Calculate date 1 week from now
    current_date = datetime.date.today()
    book_date = current_date + datetime.timedelta(days=8)
    book_date = book_date.strftime("%d-%b-%Y")

    slot_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @name="p_rec" and @value="1BB2BB0' + str(court) + book_date + str(timing-7) + '"]')))
    # slot_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="radio" and @name="p_rec" and @value="1BB2BB0623-Sep-20232"]')))
    slot_button.click()
    confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="submit" and @name="bOption" and @value="Confirm"]')))
    confirm_button.click()

    # Calculate the elapsed time
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Print the elapsed time
    print(f"Process took {elapsed_time:.4f} seconds")

    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="NH Badminton Court Booking")
    parser.add_argument("--time", type=int, default = 10, help = "intended booking time")
    parser.add_argument("--court", type=int, default= 6, help="court number")
    args = parser.parse_args()

    main(args.time,args.court)