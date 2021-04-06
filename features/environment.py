from selenium import webdriver


def before_all(context):
    context.web = webdriver.Chrome(
        executable_path='dependency/chromedriver.exe')    


def after_step(context, step):
    print()


def after_all(context):
    context.web.quit()
