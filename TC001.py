
from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')
chrome_browser.maximize_window()
chrome_browser.get('https://ze.delivery/')
chrome_browser.implicitly_wait(3)

signInBtn = chrome_browser.find_element_by_id('welcome-button-sign-in')
signInBtn.click()
chrome_browser.implicitly_wait(2)
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
brejaBtn = chrome_browser.find_element_by_xpath("(//div[@class='css-1tkwx94'])[1]").click()
chrome_browser.implicitly_wait(6)
addBtn = chrome_browser.find_element_by_xpath("(//div[@class='css-1yml8pt'])[1]").click()
chrome_browser.implicitly_wait(6)
closeBtn = chrome_browser.find_element_by_css_selector("#sidebar-header-close-button").click()




