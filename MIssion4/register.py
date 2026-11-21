from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import json


driver = webdriver.Chrome()
#Set URL for Charlotte Chess Center
url = "https://app.charlottechesscenter.org/events"


#see README for how to configure this file
cookieFile = ".env"

#open environment file and extract remember me cookies
with open (cookieFile, "r") as file:
    data = json.load(file)

#set cookie name and valuen to variables
cookieName = data["name"]
cookieContent = data["value"]
event = data["event"]
section = data["section"]

#open the Chess center webpage, and then inject the cookies
driver.get(url)
driver.add_cookie({"name":cookieName, "value":cookieContent})
driver.get(url)
wait = WebDriverWait(driver, 15)

#parse upcoming events for the exact event you would like to register for
wait.until(EC.presence_of_element_located((By.ID, "upcoming-cards")))
event_xpath = (
"//div[contains(@class, 'p-6') and .//h3[contains(., '" + event + "')]]"
"//a[contains(., 'Register')]"
)

#find the "Register" button and extract its value, this vUY
register_button = wait.until(EC.element_to_be_clickable((By.XPATH, event_xpath)))

# 5. Extract the URL
register_url = register_button.get_attribute("href")

print(f"Successfully found URL: {register_url}")

driver.get(register_url)

wait = WebDriverWait(driver, 15)

try:
    section_dropdown_element = wait.until(EC.presence_of_element_located((By.ID, "section_id")))

    #find the section selection dropdown and select our section
    section_select = Select(section_dropdown_element)

    # Select the option by the text visible to the user
    section_select.select_by_visible_text(section)
    print("Selected section: " + section)

    # Handle the Submit Button
    # We must wait for the button to become 'clickable' (which means enabled).
    submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit-btn")))

    # Click the button
    submit_button.click()
    print("Clicked the registration button. Registration completed.")

except:
    # otherwise if a section wasn't available, just register the user. 
    # This is relevant for quads and other events
    submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit-btn")))

    # Click the button
    try:
        submit_button.click()
        print("Clicked the registration/payment button. Registration completed.")
    except:
        print("Registration did not succeed because the section didn't exist or the event didn't exist")
        exit()
                    




