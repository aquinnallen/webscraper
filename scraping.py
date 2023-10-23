#from urllib.request import urlopen
#from phantomjs import Phantom

from selenium import webdriver

url = "https://www.redfin.com/city/13223/WA/Olympia/apartments-for-rent"


browser = webdriver.Firefox()
browser.get(url)
html_string = browser.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
print(html_string)
#page = urlopen(url)
#html_bytes = page.read()
#html_string = html_bytes.decode("utf-8")

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
#print(html_string)
