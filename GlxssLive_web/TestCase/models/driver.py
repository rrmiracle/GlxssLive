from selenium import webdriver


def browser():
    driver = webdriver.Chrome()
    return driver