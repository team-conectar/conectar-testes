from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


@when(u'clico no botao de buscar')
def clica_btn_busca(context):
    context.search_submit = context.web.find_element_by_xpath(
        '//*[@id="root"]/div/main/div[1]/nav/form/button')
    context.search_submit.click()


@then(u'projetos e pessoas devem ser retornadas')
def checa_retorno_projetos_pessoas(context):
    wait = WebDriverWait(context.web, 10)
    context.area_desenvolvimento = wait.until(ec.presence_of_element_located(
        (By.XPATH, '//*[@id="root"]/div/aside/h2')))
    if 'Nenhum projeto encontrado.' in context.web.page_source:
        raise Exception('Nenhum projeto foi encontrado.')


@when(u'preencho o campo de busca com um nome de pessoa/projeto existente')
def step_impl(context):
    context.search_input = context.web.find_element_by_xpath('//*[@id="root"]/div/main/div[1]/nav/form/input')
    context.search_input.send_keys('teste')