from selenium.webdriver import  Chrome
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from functools import partial


driver = Chrome('B:\chromedriver.exe') #Change the path to where your webdriver is located
driver.implicitly_wait(10)
driver.maximize_window()
URL = driver.get('http://www.globalsqa.com/angularJs-protractor/SimpleCalculator/')

def Test_title ():

    title = driver.find_element_by_xpath('/html/body/h1')
    actual_title = title.text
    print(actual_title)
    expected_title = 'AngularJS calculator'

    assert actual_title == expected_title

Test_title()

def Test_inputs():

        input_a = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[1]/td[2]/input')
        input_a.clear()
        #input_a.send_keys(input('Enter value for a = '))
        input_a.send_keys('2')
        input_b = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[2]/td[2]/input')
        input_b.clear()
        #input_b.send_keys(input('Enter value for b = '))
        input_b.send_keys('25')

Test_inputs()

def Test_increment_a():
    Inc_a = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[1]/td[3]/button[1]')
    print(Inc_a.is_enabled())
    Inc_a.click()

def Test_increment_b():
    Inc_b = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[2]/td[3]/button[1]')
    print(Inc_b.is_enabled())
    Inc_b.click()

def Test_decrement_a():
    Dec_a = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[1]/td[3]/button[2]')
    print(Dec_a.is_enabled())
    Dec_a.click()

def Test_decrement_b():
    Dec_b = driver.find_element_by_xpath('/html/body/div/table/tbody/tr[2]/td[3]/button[2]')
    print(Dec_b.is_enabled())
    Dec_b.click()

def Test_add(a = 0,b = 0):

    Op_add = Select(driver.find_element_by_xpath('/html/body/div/table/tbody/tr[3]/td[2]/select'))
    Op_add.select_by_value('+')

def Test_sub(a = 0,b = 0):

    Op_sub = Select(driver.find_element_by_xpath('/html/body/div/table/tbody/tr[3]/td[2]/select'))
    Op_sub.select_by_value('-')

def Test_mul(a = 0,b = 0):

    Op_mul = Select(driver.find_element_by_xpath('/html/body/div/table/tbody/tr[3]/td[2]/select'))
    Op_mul.select_by_value('*')

def Test_div(a = 0,b = 0):

    Op_div = Select(driver.find_element_by_xpath('/html/body/div/table/tbody/tr[3]/td[2]/select'))
    Op_div.select_by_value('/')

tasks = [
    partial(Test_add),
    partial(Test_div),
    partial(Test_mul),
    partial(Test_sub),
    partial(Test_decrement_a),
    partial(Test_increment_a),
    partial(Test_increment_b),
    partial(Test_decrement_b),
]

for task in tasks:
    task()
    time.sleep(2)



driver.quit()

