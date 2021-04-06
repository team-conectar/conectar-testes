from behave import given, when, then
import time

base_url = "https://boraconectar.com"
submit_xpath = '//*[@id="root"]/div/main/div[1]/div/section[2]/form/div[2]'


@given(u'acesso a pagina inicial do Conectar')
def abre_pagina(context):
    context.web.get(base_url)


@when(u'preencho o formulario com dados cadastrados na base')
def preenche_formulario(context):
    context.usuario_input = context.web.find_element_by_id('email')
    context.usuario_input.send_keys('francisco@gmail.com')

    context.senha_input = context.web.find_element_by_id('senha')
    context.senha_input.send_keys('Qwaszx12@')

    context.submit = context.web.find_element_by_class_name('sc-iqHYGH')
    context.submit.click()


@then(u'devo ser logado na plataforma')
def envia_formulario(context):
    time.sleep(2)
    context.usuario_icon = context.web.find_element_by_id('user')
