from selenium import webdriver
import time
if __name__=="__main__":
    driver = webdriver.Chrome()
    driver.get("https://iam-sit.immotors.com/login/")
    time.sleep(3)
