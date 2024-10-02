from selenium.webdriver.common.by import By
class Locators:
    ACCOUNT_BUTTON = By.XPATH, '//p[text()="Личный Кабинет"]' # кнопка Личный кабинет
    REGISTRATION_BUTTON = By.XPATH, '//a[text()="Зарегистрироваться"]' # Кнопка "Зарегистрироваться"
    REGISTRATION_BUTTON_FORM = By.XPATH, '//button[text()="Зарегистрироваться"]' # кнопка зарегистрироваться в форме регистрации
    NAME_INPUT = By.XPATH, '//label[text()="Имя"]/parent::div/input' # поле ввода имени
    EMAIL_INPUT = By.XPATH, '//label[text()="Email"]/parent::div/input' # поле ввода почты
    PASSWORD_INPUT = By.XPATH, '//label[text()="Пароль"]/parent::div/input' # поле ввода пароля
    ENTER_BUTTON = By.XPATH, '//button[text()="Войти"]' #кнопка войти
    NAME_PERSONAL_DATA = By.XPATH, '//label[text()="Имя"]/parent::div/input' # имя в личном кабинете
    WARNING_INCORRECT_PASSWORD = By.XPATH, '//p[text()="Некорректный пароль"]' # оповещение о некорректном пароле
    MAIN_PAGE_LOGIN = By.XPATH, '//button[text() = "Войти в аккаунт"]' # кнопка войти в аккаунт на главной
    LOGIN_PERSONAL_DATA = By.XPATH, '//label[text()="Логин"]/parent::div/input' # Логин в личном кабинете
    ENTER_IN_REGISTRATION = By.XPATH, '//a[text()="Войти"]' #кнопка войти в форме регистрации.
    RECOVER_PASSWORD = By.XPATH, '//a[text()="Восстановить пароль"]' #Кнопка восстановить пароль
    ENTRANCE_HEADER = By.XPATH, '//h2[text()="Вход"]'# надпись "Вход" на странице логина
    DESIGNER =  By.XPATH, '//p[text()="Конструктор"]' #Кнопка "Конструктор"
    ASSEMBLE_BURGER = By.XPATH, '//h1'  # Надпись "Собери бурегр"
    BUNS = By.XPATH, '//span[text()="Булки"]' # Надпись "Булки"
    LOGO = By.XPATH, '//div[@class = "AppHeader_header__logo__2D0X2"]' # логотип
    LOGOUT = By.XPATH, '//button[text()="Выход"]' # Кнопка выхода в личном кабинете
    SAUCES = By.XPATH, '//span[text()="Соусы"]' # Надпись "Соусы"
    FILLINGS = By.XPATH, '//span[text()="Начинки"]' # Надпись "Начинки"
    SELECTED_PART = By.XPATH, '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]' #выбранная секция в конструкторе

