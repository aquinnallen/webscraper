#from urllib.request import urlopen   <--- This isn't powerful enough to run the javascript in the page
#from phantomjs import Phantom    <---Selenium tutortials were better

from selenium import webdriver   #import webdriver from selenium
from selenium.webdriver.firefox.options import Options #import options for webdriver in firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#target URL
url = "https://www.redfin.com/city/13223/WA/Olympia/apartments-for-rent"

#set up headless selenium with firefox webdriver
options = Options()
#options.add_argument("-headless")
options.add_argument("--window-size=1920,1200")
browser = webdriver.Firefox(options=options)
browser.implicitly_wait(5)

browser.get(url)
#browser.find_element(By.CSS_SELECTOR, "button[data-rf-test-name*='tableOption']").click()

html_string = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
print(html_string)

"""
Depreciated by using selenium
page = urlopen(url)
html_bytes = page.read()
html_string = html_bytes.decode("utf-8")
"""

"""
You cannot parse what you haven't captured correctly


parsing = True
addresses = []
idx = 0
target = "col_address"
#print(len(html_string))
#print(html_string[0:len(html_string)+5])

while parsing:
    #print("dingdong!")
    #print(idx)
    cur_string = html_string[idx:idx+(len(target))]
    #print(cur_string)
    if cur_string == target:
        #print(idx)
        print("ding!")
        parsing = False
    #if idx == 1000:
        #parsing = False
    idx = idx + 1
"""
#print(html_string)
