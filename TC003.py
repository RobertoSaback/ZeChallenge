
from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')
chrome_browser.maximize_window()
chrome_browser.get('https://ze.delivery/')
chrome_browser.implicitly_wait(3)

signInBtn = chrome_browser.find_element_by_id('welcome-button-sign-in')
signInBtn.click()
chrome_browser.implicitly_wait(3)
# Fills email input
emailForm = chrome_browser.find_element_by_css_selector('#login-mail-input-email')
emailForm.clear()
emailForm.send_keys('zechallengeqa@gmail.com')
chrome_browser.implicitly_wait(2)
# Fills password input
passwordForm = chrome_browser.find_element_by_css_selector('#login-mail-input-password')
passwordForm.clear()
passwordForm.send_keys('1q2w3e$!')
chrome_browser.implicitly_wait(2)
# Login
enterBtn = chrome_browser.find_element_by_css_selector('#login-mail-button-sign-in').click()
chrome_browser.implicitly_wait(10)
# +18 Verification
ageVerification = chrome_browser.find_element_by_id('age-gate-button-yes').click()
# ------- Test Case -------- #
brahmaItem = chrome_browser.find_element_by_css_selector("body > div:nth-child(2) > div:nth-child(1) > div:nth-child(6) > div:nth-child(1) > div:nth-child(2) > a:nth-child(3) > div:nth-child(1) > div:nth-child(2)").click()
def brahmaAddBtn() : chrome_browser.find_element_by_css_selector('#add-amount-10').click()
i = 1
while i < 10:
    brahmaAddBtn()
    i += 1
addBtn = chrome_browser.find_element_by_xpath("//div[@class='css-1yml8pt']").click()
closeBubbleBtn = chrome_browser.find_element_by_xpath("//div[@class='css-6k9kan-header']//*[name()='svg']").click()





