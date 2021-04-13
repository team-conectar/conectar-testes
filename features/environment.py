from selenium import webdriver
import os


def before_all(context):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    context.web = webdriver.Chrome(
        executable_path='dependency/chromedriver.exe', chrome_options=chrome_options)


def after_step(context, step):
    print()


def after_all(context):
    context.web.quit()
