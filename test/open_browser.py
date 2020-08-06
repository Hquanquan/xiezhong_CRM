from selenium import webdriver

browser = webdriver.Chrome(r'E:\python\chromedriver_win32\chromedriver.exe')

browser.maximize_window()

browser.get('https://www.baidu.com/')