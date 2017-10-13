from selenium import webdriver


def browser():
    driver = webdriver.Firefox()
    return driver