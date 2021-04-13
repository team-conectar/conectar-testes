from behave import given, when, then
from utils.data_generator import name_generator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@when(u'clico no botao para cadastrar um novo projeto')
def clica_btn_novo_projeto(context):
    context.cadastro_projeto_btn = context.web.find_element_by_class_name(
        'create')
    context.cadastro_projeto_btn.click()


@when(u'preencho a etapa um do formulario de cadastro de projeto')
def preenche_etapa1_formulario(context):
    context.nome_input = context.web.find_element_by_id('nome')
    context.nome_input.send_keys(name_generator())

    wait = WebDriverWait(context.web, 3)
    context.area_desenvolvimento = wait.until(ec.presence_of_element_located(
        (By.XPATH, '//*[@id="root"]/div/main/form/div[2]/div/div/div[2]/ul/li[1]')))

    context.area_desenvolvimento.click()

    context.area_desenvolvimento_especifica = context.web.find_element_by_xpath(
        '//div[@class="area-selecao"]/aside/ul/li')
    context.area_desenvolvimento_especifica.click()

    context.continuar_btn = context.web.find_element_by_xpath(
        '//*[@id="root"]/div/main/form/section/button[2]')
    context.continuar_btn.click()


@then(u'devo ser redirecionado para a segunda etapa')
def checa_segunda_etapa_cadastro(context):
    if 'Ferramentas, matérias e habilidades que o time precisa dominar' not in context.web.page_source:
        raise Exception(
            'Texto "Ferramentas, matérias e habilidades que o time precisa dominar" era esperado e não foi encontrado.')
