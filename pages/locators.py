from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT = (By.CSS_SELECTOR, "[id='id_registration-email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[id='id_registration-password1']")
    PASSWORD_INPUT2 = (By.CSS_SELECTOR, "[id='id_registration-password2']")
    REGISTER_BTN = (By.CSS_SELECTOR, '[name="registration_submit"]')

class ProductPageLocators():
    PRODUCT_BUTTON = (By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-add-to-basket"]')
    PRODUCT_NAME = (By.TAG_NAME, 'h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '[class="price_color"]')
    BUCKET_PRICE = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    PRODUCT_NAME_IN_BUCKET = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.XPATH, '//*[@class="btn-group"]/a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    EMPTY_BASKET_TEXT = (By.XPATH, '//*[@id="content_inner"]/p')
    CONTINUE_BUTTON = (By.XPATH, "//*[@id='content_inner']/p/a")