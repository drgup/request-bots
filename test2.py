from selenium import webdriver
from selenium.webdriver.support.select import Select 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(executable_path='/Users/manneetu/Application/chromedriver')
wait=WebDriverWait(driver,2)

buyerName='Dru Gupta'
buyerMail='dhruv6gupta@yahoo.com'
buyerTele='858 382 1709'
buyerAdress='12407 Mesa Vista Place'
buyerZIP='92131'
buyerState='CA'
buyerCardNumber='4060 6870 4006 200'
buyerCardExpMonth='11'
buyerCardExpYear='2020'
buyerOrcer='771'

#go to website
driver.get('http://www.supremenewyork.com/shop/all/accessories')

while True:
 try:
  driver.find_element_by_partial_link_text('Supreme')
  break
 except (NoSuchElementException):
  wait=WebDriverWait(driver, 10)
  waitBis=wait.until(EC.presence_of_element_located((By.ID, 'time-zone-name')))
  driver.refresh()

#find item
driver.find_element_by_partial_link_text('Hanes').click()
print("item found")

#add to cart
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-remove-buttons"]/input'))).click()
print("added to cart")

#go to checkout
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cart"]/a[2]'))).click()
print("going to checkout")

#filling/processing
order_billing_name=driver.find_element_by_xpath('//*[@id="order_billing_name"]')
order_billing_name.send_keys(buyerName)
order_email=driver.find_element_by_xpath('//*[@id="order_email"]')
order_email.send_keys(buyerMail)
order_tele=driver.find_element_by_xpath('//*[@id="order_tel"]')
order_tele.send_keys(buyerTele)
order_adress=driver.find_element_by_xpath('//*[@id="bo"]')
order_adress.send_keys(buyerAdress)
order_zip=driver.find_element_by_xpath('//*[@id="order_billing_zip"]')
order_zip.send_keys(buyerZIP)
Select(driver.find_element_by_xpath('//*[@id="order_billing_state"]')).select_by_visible_text(buyerState)
order_cnb=driver.find_element_by_xpath('//*[@id="nnaerb"]')
order_cnb.send_keys(buyerCardNumber)
Select(driver.find_element_by_xpath('//*[@id="credit_card_month"]')).select_by_visible_text(buyerCardExpMonth)
Select(driver.find_element_by_xpath('//*[@id="credit_card_year"]')).select_by_visible_text(buyerCardExpYear)
orcer=driver.find_element_by_xpath('//*[@id="orcer"]')
orcer.send_keys(buyerOrcer)
order_terms=driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins')
order_terms.click()
driver.find_element_by_xpath('//*[@id="pay"]/input').click()
print("checked out!")

#google/captcha
#options=webdriver.ChromeOptions()
#options.add_argument('/Users/manneetu/Library/Application Support/Google/Chrome/Default')

#driver=webdriver.Chrome(executable_path=chrome_path, chrome_options=options)

#driver.get('http://www.supremenewyork.com/')

