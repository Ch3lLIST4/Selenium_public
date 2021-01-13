from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
import tldextract
import sys


# browser/driver paths
BROWSER_PATH = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
DRIVER_PATH = "../chromedriver_win32/chromedriver.exe"

# image path
SCREENSHOT_PATH = "./screenshots/"

# set browser's components
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.binary_location = BROWSER_PATH
chrome_driver_binary = DRIVER_PATH

try:

    # declare target url
    target = sys.argv[1].strip()

    # get hostname for creating filename 
    ext = tldextract.extract(target)
    domain = ext.registered_domain
    hostname = '.'.join(part for part in ext if part)

    # 1. load driver
    browser = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

    # 2. go to webpage
    browser.get(target)
    time.sleep(1)

    # 3. take screenshot
    file_path = SCREENSHOT_PATH + str(hostname) + str(datetime.datetime.now().strftime("_%d%m%Y_%H%M")) + ".png"
    browser.get_screenshot_as_file(file_path)
    print('screenshot saved at :', file_path)

except IndexError as error:
    print("""
Usage: python capture.py address
    """)
except Exception as e:
    print(str(e))
