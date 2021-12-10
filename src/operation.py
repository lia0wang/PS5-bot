'''
v0.5.0.5 ps5 Bot only for Amazon
powered by https://github.com/lia0wang
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Initialise options.
options = Options()
options.headless = False
options.add_argument("--window-size=0.5920,0.5200")

# Find the path of chrome.
path = ChromeDriverManager().install()
driver = webdriver.Chrome(path, options=options)

# Store the user infomation, u can replace below infomation
user_dict = {
    # Delete the info below and change to you own
    'firs_name': 'Your first name',
    'last_name': 'Your second name',
    'email': 'Your email',
    'number': 'Your phone number',
    'password': 'Your password',
    'postcode': 'Your postcode',
    'card_number': 'Your card number',
    'csv': 'Your csv'
}

# Site
Amazon = "https://www.amazon.com.au/PxlayStation-5-Console/dp/B08HHV8945"
BigW = "https://www.bigw.com.au/product/playstation-5-console/p/124625"
test = "https://www.bigw.com.au/product/ps5-dualsense-charging-station/p/124628"

def Amazon_bot(got_it):
    try:
        driver.get(Amazon)

        add_chart = driver.find_element_by_xpath("//*[@id='add-to-cart-button']")
        add_chart.click()
        sleep(0.5)

        check_out = driver.find_element_by_xpath("//*[@id='hlb-ptc-btn-native']")
        check_out.click()
        sleep(0.5)

        sign_in = driver.find_element_by_xpath("//*[@id='ap_email']")
        sign_in.send_keys(user_dict['number'])
        sleep(0.5)

        continue_but = driver.find_element_by_xpath("//*[@id='continue']")
        continue_but.click()
        sleep(0.5)

        enter_password = driver.find_element_by_xpath("//*[@id='ap_password']")
        enter_password.send_keys(user_dict['password'])
        sleep(0.5)

        ensure_password = driver.find_element_by_xpath("//*[@id='signInSubmit']")
        ensure_password.click()
        sleep(0.5)

        place_order = driver.find_element_by_xpath("//*[@id='submitOrderButtonId']/span/input")
        place_order.click()
        return True
    except:
        sleep(0.5)
        return False

def BigW_bot(got_it, log_in_bigW):
    try:

        driver.get(BigW)

        add_chart = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/main/div/div[1]/div[2]/div[8]/div[1]/button[1]')
        add_chart.click()

        sleep(1)
        postcode = driver.find_element_by_xpath('//*[@id="react-select-2-input"]')
        postcode.send_keys(user_dict['postcode'])
        sleep(1)
        postcode.send_keys(webdriver.common.keys.Keys.ENTER)
        sleep(1)
        save = driver.find_element_by_xpath('/html/body/div[12]/div/div/div/div/div[3]/button')
        save.click()
        sleep(0.5)

        driver.execute_script("window.scrollTo(0, 500)") 
        sleep(0.5)

        add_char_new = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/main/div/div[1]/div[2]/div[8]/div/div[1]/div[3]/button[1]')
        add_char_new.click()
        sleep(0.1)

        driver.execute_script("window.scrollTo(0, 0)") 
        sleep(1.5)

        go_cart = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/header/div[2]/div[2]/button[2]')
        go_cart.click()
        sleep(0.1)

        check_out = driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/main/div[2]/div/div[2]/section/div[5]/button')
        check_out.click()
        sleep(1)

        check_out_email = driver.find_element_by_xpath('//*[@id="login__email"]')
        check_out_email.send_keys(user_dict['email'])
        checkout_password = driver.find_element_by_xpath('//*[@id="login__password"]')
        checkout_password.send_keys(user_dict['password'])
        log_in_new = driver.find_element_by_xpath('//*[@id="login"]/button')
        log_in_new.click()
        sleep(2)

        driver.execute_script("window.scrollTo(0, 1000)")
        sleep(0.5)

        process_to_payment = driver.find_element_by_xpath('//*[@id="delivery-form-id"]/div/div/button')
        process_to_payment.click()
        sleep(2)

        driver.execute_script("window.scrollTo(0, 800)")
        sleep(0.5)

        select_payment_method = driver.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[3]/section/section/section[2]/div[2]/section/div[2]/header/section')
        select_payment_method.click()
        sleep(0.1)

        input_csv = driver.find_element_by_xpath('//*[@id="saved-cards__cv2"]')
        # input_csv.send_keys(user_dict['csv'])
        sleep(0.1)

        ensure_payment = driver.find_element_by_xpath('//*[@id="saved-cards"]/div[3]/button')
        ensure_payment.click()
        sleep(0.1)

        driver.delete_all_cookies()

        return True, log_in_bigW

    except:
        driver.delete_all_cookies()
        sleep(0.5)
        return False, log_in_bigW

def bot_run():
    got_it = False
    round = 1
    log_in_bigW = False
    while not got_it:
        print(f"Scanning from Amazon {round} time...")
        print("---------------------")
        got_it = Amazon(got_it)
        if got_it:
            print("You got this sht!")
            print("---------------------")
            break
        print("Cannot find a ps5 from Amazon.")
        print("---------------------")

        print(f"Scanning from BigW {round} time...")
        print("---------------------")
        got_it, log_in_bigW = BigW_bot(got_it, log_in_bigW)

        if got_it:
            print("You got this sht!")
            print("---------------------")
            # break
        print("Cannot find a ps5 from BigW.")
        print("---------------------")


        round += 1

    driver.close()
