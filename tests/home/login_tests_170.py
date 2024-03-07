from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class LoginTests():

    def test_validLogin(self):
        baseURL = "https://www.letskodeit.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)


        loginLink = driver.find_element(By.XPATH, "(//a[@class='dynamic-link' and text()='Sign In'])")
        loginLink.click()

        emailField = driver.find_element(By.XPATH, "(//input[@type='email' and @placeholder='Email Address'])")
        emailField.send_keys("test@email.com")

        passwordField = driver.find_element(By.XPATH, "(//input[@type='password'])")
        passwordField.send_keys("abcabc")

        time.sleep(3)

        loginButton = driver.find_element(By.XPATH, "(//button[@id='login'])")
        loginButton.click()

        userIcon = driver.find_element(By.XPATH, "(//div[@class='dropdown']//span[text()='My Account'])")
        if userIcon is not None:
            print("Login is successful")
        else:
            print("Login Failed")

        driver.quit()

ff = LoginTests()
ff.test_validLogin()
