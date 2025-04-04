from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configure Chrome for Termux (if using Chrome)
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in background (optional)
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Initialize WebDriver (replace with your chromedriver path)
driver = webdriver.Chrome(executable_path='/data/data/com.termux/files/usr/bin/chromedriver', options=options)

def report_post(post_url):
    try:
        # Open Facebook post
        driver.get(post_url)
        time.sleep(5)  # Wait for page load

        # Click the 3-dot menu
        dots_menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@aria-label='More options']"))
        )
        dots_menu.click()
        time.sleep(2)

        # Click "Find support or report post"
        report_option = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Find support or report post')]"))
        )
        report_option.click()
        time.sleep(2)

        # Select a reason (e.g., "Spam")
        spam_option = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Spam')]"))
        )
        spam_option.click()
        time.sleep(2)

        # Submit report
        submit_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Submit')]"))
        )
        submit_btn.click()
        time.sleep(2)

        print("[SUCCESS] Post reported successfully!")
    
    except Exception as e:
        print("[ERROR] Failed to report post: {}".format(e))  # Python 2 compatible

# Example usage (replace with a real post URL)
post_url = "https://www.facebook.com/example-post"
report_post(post_url)

# Close the browser
driver.quit()
