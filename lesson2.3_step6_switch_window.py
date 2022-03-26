from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    magick_button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    magick_button.click()
    
    window2 = browser.window_handles[1] # ищем новое окно 
    browser.switch_to.window(window2) # переключаемся на новое окно
    
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()    
    print(browser.switch_to.alert.text)

finally:
    
    browser.quit()