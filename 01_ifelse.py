import time
from selenium import webdriver

#set instance for chrome browser
browser = webdriver.Chrome()

#open webpage
browser.maximize_window()
browser.get("https://weathershopper.pythonanywhere.com/")

#verify title
if (browser.title=="Current Temperature"):
    print("Success, page opened")
else:
    print("Failed to open webpage")

temperature = browser.find_element_by_xpath("//span[@id='temperature']")
temp = temperature.text
browser.implicitly_wait(10)

#:2 will take the numbers ie first two and leave the degree and c
D= int(temp[:2])
print('Temperature is ',D)
browser.implicitly_wait(10)

if(D  < 19):
    print('Temprature is less than 19')
    moisturizers = browser.find_element_by_xpath("//button[contains(text(),'Buy moisturizers')]")
    moisturizers.click()

elif(D > 34):
    print('Temprature is greater than 45')
    sunscreen = browser.find_element_by_xpath("//button[contains(text(),'Buy sunscreens')]")
    sunscreen.click()
















