
from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')
chrome_browser.maximize_window()
chrome_browser.get('https://ze.delivery/')
chrome_browser.implicitly_wait(3)

signInBtn = chrome_browser.find_element_by_id('welcome-button-sign-in')
signInBtn.click()
chrome_browser.implicitly_wait(6)
# Fills email input
emailForm = chrome_browser.find_element_by_css_selector('#login-mail-input-email')
emailForm.clear()
emailForm.send_keys('zechallengeqa@gmail.com')
chrome_browser.implicitly_wait(6)
# Fills password input
passwordForm = chrome_browser.find_element_by_css_selector('#login-mail-input-password')
passwordForm.clear()
passwordForm.send_keys('1q2w3e$!')
chrome_browser.implicitly_wait(2)
# Login
enterBtn = chrome_browser.find_element_by_css_selector('#login-mail-button-sign-in').click()
chrome_browser.implicitly_wait(6)
# +18 Verification
ageVerification = chrome_browser.find_element_by_id('age-gate-button-yes').click()
# ------- Test Case -------- #
# Beers
beers = chrome_browser.find_element_by_css_selector("div[id='category-Cervejas'] div[class='css-1q0ig7m-categoryContent']").click()
brahma = chrome_browser.find_element_by_css_selector("#image-brand-Brahma").click()
puroMalte = chrome_browser.find_element_by_xpath("(//div[@class='css-1tkwx94'])[1]").click()
def brahmaAddBtn() : chrome_browser.find_element_by_css_selector('#add-amount-10').click()
i = 1
while i < 10:
    brahmaAddBtn()
    i += 1
addBtn = chrome_browser.find_element_by_xpath("//div[@class='css-1yml8pt']").click()
closeBubbleBtn = chrome_browser.find_element_by_xpath("//div[@class='css-6k9kan-header']//*[name()='svg']").click()
# Spirits
spirits = chrome_browser.find_element_by_css_selector("div[id='category-Destilados'] div[class='css-1d2xvqe-categoryText']").click()
beats = chrome_browser.find_element_by_css_selector("#image-brand-Beats").click()
beatsPack = chrome_browser.find_element_by_css_selector("a[title='Beats Senses 269ml - Pack de 8 unidades'] div[class='css-1tkwx94']").click()

def beatsAddBtn() : chrome_browser.find_element_by_css_selector('#add-amount-10').click()
i = 1
while i < 10:
    beatsAddBtn()
    i += 1
addBtn = chrome_browser.find_element_by_xpath("//div[@class='css-1yml8pt']").click()
closeBubbleBtn = chrome_browser.find_element_by_xpath("//div[@class='css-6k9kan-header']//*[name()='svg']").click()
# Wines
wines = chrome_browser.find_element_by_css_selector("#category-Vinhos").click()
whiteWine = chrome_browser.find_element_by_xpath("(//img[@id='image-brand-Vinhos Brancos'])[1]").click()
foye = chrome_browser.find_element_by_xpath("(//div[@class='css-1tkwx94'])[4]").click()

def wineAddBtn() : chrome_browser.find_element_by_css_selector('#add-amount-10').click()
i = 1
while i < 10:
    wineAddBtn()
    i += 1
addBtn = chrome_browser.find_element_by_xpath("//div[@class='css-1yml8pt']").click()
closeBubbleBtn = chrome_browser.find_element_by_xpath("//div[@class='css-6k9kan-header']//*[name()='svg']").click()
# No Alchool
noAchool = chrome_browser.find_element_by_xpath("(//div[@id='category-Sem Álcool'])[1]").click()
redBull = chrome_browser.find_element_by_css_selector("a[title='Red Bull Energy Drink 250ml - Pack 4 unidades'] div[class='css-1tkwx94']").click()
def redBullAddBtn() : chrome_browser.find_element_by_css_selector('#add-amount-10').click()
i = 1
while i < 10:
    redBullAddBtn()
    i += 1
addBtn = chrome_browser.find_element_by_xpath("//div[@class='css-1yml8pt']").click()
closeBubbleBtn = chrome_browser.find_element_by_xpath("//div[@class='css-6k9kan-header']//*[name()='svg']").click()

