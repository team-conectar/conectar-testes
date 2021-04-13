from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec
import time
from utils.data_generator import name_generator, email_generator, username_generator, password_generator


@when(u'clico no botao de cadastro')
def step_impl(context):
    context.cadastro_btn = context.web.find_element_by_xpath(
        '//*[@id="root"]/div/main/div[1]/div/section[2]/form/p[2]/a')
    context.cadastro_btn.click()


@when(u'preencho a primeira etapa do formulario de cadastro com dados não cadastrados na base')
def preenche_etapa1_formulario(context):

    context.nome_input = context.web.find_element_by_id('nome')
    context.nome_input.send_keys(name_generator())

    context.email_input = context.web.find_element_by_id('email')
    context.email_input.send_keys(email_generator())

    context.username_input = context.web.find_element_by_id('username')
    context.username_input.send_keys(username_generator())

    context.password_input = context.web.find_element_by_id('password')
    context.password_input.send_keys(password_generator())

    context.submit = context.web.find_element_by_xpath(
        '/html/body/div[1]/div/form/div/div/section[2]/button')
    context.submit.click()


@then(u'devo ser registrado na plataforma e enviado para a segunda etapa')
def checa_segunda_etapa_cadastro(context):
    wait = WebDriverWait(context.web, 3)
    wait.until(ec.visibility_of_element_located(
        (By.CLASS_NAME, 'segunda-etapa')), message='Painel de "Segunda Etapa" era esperado e não foi encontrado.')


@given(u'estou na pagina da segunda etapa do cadastro')
def checa_pagina_segunda_etapa(context):
    context.usuario_icon = context.web.find_element_by_class_name(
        'segunda-etapa')


@when(u'preencho a segunda etapa do formulario de cadastro')
def preenche_etapa2_formulario(context):
    context.telefone_input = context.web.find_element_by_id('telefone')
    context.telefone_input.send_keys('46999999999')

    context.year_arrow = context.web.find_element_by_xpath(
        '//*[@id="root"]/div/form/div/section[1]/div[2]/label/div/div/div[2]')
    context.year_arrow.click()

    context.year_input = context.web.find_element_by_id('year')
    context.year_input.send_keys(1990)

    wait = WebDriverWait(context.web, 3)
    wait.until(ec.element_to_be_clickable(
        (By.CSS_SELECTOR, 'div.react-select__menu')), message='Select de "Ano" era esperado e não foi encontrado.')

    context.year_selector = context.web.find_element_by_css_selector(
        'div.react-select__menu')

    context.year_option = context.web.find_element_by_xpath(
        '//div[contains(@class, "react-select__option")]')
    context.year_option.click()

    context.month_input = context.web.find_element_by_id('month')
    context.month_input.send_keys(5)

    wait = WebDriverWait(context.web, 3)
    wait.until(ec.element_to_be_clickable(
        (By.CSS_SELECTOR, 'div.react-select__menu')), message='Select de "Mês" era esperado e não foi encontrado.')

    context.year_selector = context.web.find_element_by_css_selector(
        'div.react-select__menu')

    context.year_option = context.web.find_element_by_xpath(
        '//div[contains(@class, "react-select__option")]')
    context.year_option.click()

    context.month_input = context.web.find_element_by_id('day')
    context.month_input.send_keys(5)

    wait = WebDriverWait(context.web, 3)
    wait.until(ec.element_to_be_clickable(
        (By.CSS_SELECTOR, 'div.react-select__menu')), message='Select de "Dia" era esperado e não foi encontrado.')

    context.year_selector = context.web.find_element_by_css_selector(
        'div.react-select__menu')

    context.year_option = context.web.find_element_by_xpath(
        '//div[contains(@class, "react-select__option")]')
    context.year_option.click()

    context.idealizador_check = context.web.find_element_by_xpath(
        '/html/body/div[1]/div/form/div/section[2]/fieldset[1]/aside/div/label')
    context.idealizador_check.click()

    context.continuar_btn = context.web.find_element_by_xpath(
        '/html/body/div[1]/div/form/div/section[3]/button[2]')
    context.continuar_btn.click()


@then(u'devo ser redirecionado para a terceira etapa')
def checa_terceira_etapa_cadastro(context):
    if 'Nos conte sua experiência' not in context.web.page_source:
        raise Exception(
            'Texto "Nos conte sua experiência" era esperado e não foi encontrado.')
