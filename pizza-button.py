from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from enum import Enum
import time

### pizza object definitions 

Topping = Enum('Toppings','Pepperoni Sausage Onions Olives')
Crust = Enum('Crust','Regular GlutenFree')
Size = Enum('Size','Small Medium Large ExtraLarge')
class Address:
    def __init__(self, address1, address2, city, state, zipCode):
        self.AddressLine1 = address1
        self.AddressLine2 = address2
        self.City = city
        self.State = state
        self.ZipCode = zipCode

class Order:
    def __init__(self, address, toppings, crust, size):
        self.Address = address
        self.Toppings = toppings
        self.Crust = crust
        self.Size = size

homeAddress = Address("315 Belmont Ave E","Apt 204","Seattle","WA","98102")
order = Order(homeAddress,[Topping.Pepperoni,Topping.Onions],Crust.GlutenFree,Size.Large)


###### Here begins the ordering code

driver = webdriver.Firefox()
driver.get("https://weborder.zeekspizza.com/default.aspx")

def sendStringToID(driver,idString,inputString):
    element = driver.find_element_by_id(idString)
    element.send_keys(inputString)

def sendClickToID(driver,idString):
    element = driver.find_element_by_id(idString)
    element.click()

def loginPage(driver):
    driver.switch_to_frame("rightMargin")
    sendStringToID(driver,"_username","themeanvaluetheorem@gmail.com")
    sendStringToID(driver,"_password","tM3mU5&y%wpQwn8s")
    sendClickToID(driver,"_orderType_0")
    sendClickToID(driver,"LoginButton")

loginPage(driver)

def deliveryPage(driver,address):
    driver.switch_to_frame("content")
    sendStringToID(driver,"_streetAddress",address.AddressLine1)
    sendStringToID(driver,"_unit",address.AddressLine2)
    sendStringToID(driver,"_city",address.City)
    sendStringToID(driver,"_state",address.State)
    sendStringToID(driver,"_postalZip",address.ZipCode)
    sendClickToID(driver,"saveAddressAndContinue")
    
time.sleep(5)
deliveryPage(driver,order.Address)