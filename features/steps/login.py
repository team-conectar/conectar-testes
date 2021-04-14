from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

base_url = "https://boraconectar.com"
submit_xpath = '//*[@id="root"]/div/main/div[1]/div/section[2]/form/div[2]'


@given(u'acesso a pagina inicial do Conectar')
def abre_pagina(context):
    context.web.get(base_url)


@when(u'preencho o formulario de login com dados cadastrados na base')
def preenche_formulario(context):
    context.usuario_input = context.web.find_element_by_id('email')
    context.usuario_input.send_keys('francisco@gmail.com')

    context.senha_input = context.web.find_element_by_id('senha')
    context.senha_input.send_keys('Qwaszx12@')


@when(u'clico no botao de logar')
def step_impl(context):
    context.login_btn = context.web.find_element_by_xpath(
        '//*[@id="root"]/div/main/div[1]/div/section[2]/form/button')
    context.login_btn.click()


@then(u'devo ser logado na plataforma')
def checa_icone_usuario_logado(context):
    wait = WebDriverWait(context.web, 3)
    wait.until(ec.visibility_of_element_located(
        (By.ID, 'user')), message='Ícone de id "user" era esperado e não foi encontrado.')


@then(u'devo ser redirecionado para a página Explorar')
def checa_redirecionado_explorar(context):
    wait = WebDriverWait(context.web, 3)
    wait.until(ec.url_contains('/explorar'),
               message='Rota "/explorar" era esperada e não foi encontrada.')
