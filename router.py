#!/usr/bin/env python
# coding=utf-8
import getopt
import os
from selenium import webdriver
import sys
import time


RESET_FLAGS = ["-r", "--reset"]
WIFI_FLAGS = ["-w", "--wifi"]
WIFI_OPTIONS = ["on", "off"]


def reset_connection(driver):
    # Click on 'Internet (ADSL, Fibra, 3G)' submenu item
    driver.find_elements_by_xpath("//div[@id = 'submenu2']//tr[1]")[0].click()
    # Click on 'Reset connection' button
    driver.find_element_by_id("linkbutt3").click()


def change_wifi_status(driver, arg):
    # Click on 'WIFI configuration' submenu item
    driver.find_elements_by_xpath("//div[@id = 'submenu2']//tr[4]")[0].click()
    # Enable or disable wifi
    checkbox = driver.find_element_by_name("wifistatus")
    if arg == "on" and not checkbox.is_selected():
        checkbox.click()
    elif arg == "off" and checkbox.is_selected():
        checkbox.click()
    # Click on 'Save' button
    driver.find_element_by_id("linkbutt2").click()


def exit_with_error():
    print("Usage: router.py [-r] [-w (on|off)]")
    sys.exit(2)


def check_valid_options(opts):
    if len(opts) == 0:
        return False
    for opt, arg in opts:
        if opt in WIFI_FLAGS and arg not in WIFI_OPTIONS:
            return False
    return True


# Get the specified actions
try:
    opts, _ = getopt.getopt(sys.argv[1:], "rw:", ["reset", "wifi="])
    if not check_valid_options(opts):
        exit_with_error()
except getopt.GetoptError:
    exit_with_error()
# Start the browser and enter the password
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(os.environ["ROUTER_UI_URL"])
passwd = driver.find_element_by_name("authpasswd")
passwd.send_keys(os.environ["ROUTER_UI_PASSWD"])
passwd.submit()
# Click on 'Configuration' tab
driver.find_element_by_id("rubric2").click()
# Click on 'Livebox' menu item
driver.find_elements_by_xpath("//div[@id = 'menu']/table[2]//td[@class = 'title']")[0].click()
# Perform specified actions
for opt, arg in opts:
    if opt in RESET_FLAGS:
        reset_connection(driver)
    elif opt in WIFI_FLAGS and arg in WIFI_OPTIONS:
        change_wifi_status(driver, arg)
# Close browser and exit
time.sleep(1)
driver.quit()
sys.exit()
