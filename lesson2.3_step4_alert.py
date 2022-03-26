from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/alert_accept.html'

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    button1 = browser.find_element(By.CLASS_NAME, 'btn')
    button1.click()
    
    browser.switch_to.alert.accept() # принимаем алерт без назначения переменной
    
    
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    button2 = browser.find_element(By.CLASS_NAME, 'btn')
    button2.click()
    
    alert2 = browser.switch_to.alert # в этот раз назначаем переменную и вытаскиваем из нее текст  (можно сделать как в первом варианте) 
    code = alert2.text
    print(code)
    
finally:
    browser.quit()
    