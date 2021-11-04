'''
v1.1 ps5 Bot only for Amazon
powered by https://github.com/lia0wang
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Initialise options.
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

# Find the path of chrome.
path = ChromeDriverManager().install()
driver = webdriver.Chrome(path)

# Store the user infomation, u can replace below infomation
user_dict = {
    # Delete the info below and change to you own
    'firs_name': 'Your first name',
    'last_name': 'Your second name',
    'email': 'Your email',
    'number': 'Your phone number',
    'password': 'Your password',
    'postcode': 'Your postcode',
    'card_number': 'Your card number'
}

# Site
Amazon = "https://www.amazon.com.au/PlayStation-5-Console/dp/B08HHV8945"

def Amazon_bot(got_it):
    try:
        driver.get(Amazon)

        add_chart = driver.find_element_by_xpath("//*[@id='add-to-cart-button']")
        add_chart.click()
        sleep(1)

        check_out = driver.find_element_by_xpath("//*[@id='hlb-ptc-btn-native']")
        check_out.click()
        sleep(1)

        sign_in = driver.find_element_by_xpath("//*[@id='ap_email']")
        sign_in.send_keys(user_dict['number'])
        sleep(2)

        continue_but = driver.find_element_by_xpath("//*[@id='continue']")
        continue_but.click()
        sleep(0.5)

        enter_password = driver.find_element_by_xpath("//*[@id='ap_password']")
        enter_password.send_keys(user_dict['password'])
        sleep(2)

        ensure_password = driver.find_element_by_xpath("//*[@id='signInSubmit']")
        ensure_password.click()
        sleep(1)

        place_order = driver.find_element_by_xpath("//*[@id='submitOrderButtonId']/span/input")
        place_order.click()
        return True
    except:
        sleep(1)
        return False

def bot_run():
    got_it = False
    while not got_it:
        print("Scanning from Amazon...")
        print("---------------------")
        got_it = Amazon_bot(got_it)
        if got_it:
            print("You got this sht!")
            print("---------------------")
            break
        print("Cannot find a ps5")
        print("---------------------")
    driver.close()
    