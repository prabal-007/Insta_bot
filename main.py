from time import sleep

class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password,browser):
        username_input = self.browser.find_element_by_css_selector("input[name='username']")
        password_input = self.browser.find_element_by_css_selector("input[name='password']")
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        sleep(5)

class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/login')
    def go_to_login_page(self):
        self.browser.find_element_by_class_name("tdiEy").click()
        sleep(2)
        return LoginPage(self.browser)


from selenium import webdriver

browser = webdriver.Firefox()
browser.implicitly_wait(5)

def test_login_page(browser):
    home_page = HomePage(browser)
    login_page = home_page.go_to_login_page()
    login_page.login('username','password',browser)

    errors = browser.find_elements_by_css_selector('#error_message')
    assert len(errors) == 0
test_login_page(browser)
browser.close()
