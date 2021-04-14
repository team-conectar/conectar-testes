from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec
import time
from utils.data_generator import name_generator, email_generator, username_generator, password_generator, description_generator


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
        '//*[@id="root"]/div/form/div/section[2]/fieldset[1]/aside/div/label')
    context.idealizador_check.click()

    context.continuar_btn = context.web.find_element_by_xpath(
        '//*[@id="root"]/div/form/div/section[3]/button[2]')
    context.continuar_btn.click()


@then(u'devo ser redirecionado para a terceira etapa')
def checa_terceira_etapa_cadastro(context):
    wait = WebDriverWait(context.web, 3)
    wait.until(ec.visibility_of_element_located(
        (By.CLASS_NAME, 'experiencias-do-usuario')), message='Elemento com a classe "experiencias-do-usuario" era esperado e não foi encontrado.')


@given(u'estou na pagina da terceira etapa do cadastro')
def checa_pagina_terceira_etapa(context):
    if 'Nos conte sua experiência' not in context.web.page_source:
        raise Exception(
            'Texto "Nos conte sua experiência" era esperado e não foi encontrado.')


@when(u'clico no botao de adicionar cadastro de Educação')
def clica_adicionar_educacao(context):
    context.adicionar_educacao = context.web.find_element_by_xpath(
        '//*[@id="root"]/div/div/section[1]/h2/button')
    context.adicionar_educacao.click()


@when(u'preencho a etapa de Educação do formulario de cadastro')
def preenche_educacao_formulario(context):
    context.instituicao_input = context.web.find_element_by_id('instituicao')
    context.instituicao_input.send_keys(name_generator())

    context.curso_input = context.web.find_element_by_id('curso')
    context.curso_input.send_keys(name_generator())

    context.descricao_input = context.web.find_element_by_id('descricao')
    context.descricao_input.send_keys(description_generator())

    context.concluido_check = context.web.find_element_by_xpath(
        '//*[@id="root"]/div/div/section[1]/form/aside/section[3]/div/label[3]')
    context.concluido_check.click()

    # Nível Formação
    context.nivel_formacao_arrow = context.web.find_element_by_xpath(
        '//*[@id="root"]/div/div/section[1]/form/aside/section[2]/div/label/div/div/div[2]')
    context.nivel_formacao_arrow.click()

    context.nivel_formacao_input = context.web.find_element_by_id(
        'escolaridade')
    context.nivel_formacao_input.send_keys('Mestrado')

    wait = WebDriverWait(context.web, 3)
    wait.until(ec.element_to_be_clickable(
        (By.CSS_SELECTOR, 'div.react-select__menu')), message='Select de "Nível de Formação" era esperado e não foi encontrado.')

    context.nivel_formacao_selector = context.web.find_element_by_css_selector(
        'div.react-select__menu')

    context.nivel_formacao_option = context.web.find_element_by_xpath(
        '//div[contains(@class, "react-select__option")]')
    context.nivel_formacao_option.click()

    # Ano Inicial
    context.ano_inicial_arrow = context.web.find_element_by_xpath(
        '//*[@id="root"]/div/div/section[1]/form/aside/section[2]/aside/div[1]/label/div/div/div[2]')
    context.ano_inicial_arrow.click()

    context.ano_inicial_input = context.web.find_element_by_id('data_inicio')
    context.ano_inicial_input.send_keys(1990)

    wait = WebDriverWait(context.web, 3)
    wait.until(ec.element_to_be_clickable(
        (By.CSS_SELECTOR, 'div.react-select__menu')), message='Select de "Ano Inicial" era esperado e não foi encontrado.')

    context.ano_inicial_selector = context.web.find_element_by_css_selector(
        'div.react-select__menu')

    context.ano_inicial_option = context.web.find_element_by_xpath(
        '//div[contains(@class, "react-select__option")]')
    context.ano_inicial_option.click()

    # Ano Final
    context.ano_final_arrow = context.web.find_element_by_xpath(
        '//*[@id="root"]/div/div/section[1]/form/aside/section[2]/aside/div[2]/label/div/div/div[2]/div')
    context.ano_final_arrow.click()

    context.ano_final_input = context.web.find_element_by_id('data_fim')
    context.ano_final_input.send_keys(1995)

    wait = WebDriverWait(context.web, 3)
    wait.until(ec.element_to_be_clickable(
        (By.CSS_SELECTOR, 'div.react-select__menu')), message='Select de "Ano Final" era esperado e não foi encontrado.')

    context.ano_final_selector = context.web.find_element_by_css_selector(
        'div.react-select__menu')

    context.ano_final_option = context.web.find_element_by_xpath(
        '//div[contains(@class, "react-select__option")]')
    context.ano_final_option.click()


@when(u'clico no botao de salvar cadastro de Educação')
def clica_salvar_educacao(context):
    context.salvar_educacao = context.web.find_element_by_xpath(
        '//*[@id="root"]/div/div/section[1]/form/aside/section[5]/button[1]')
    context.salvar_educacao.click()


@then(u'uma nova experiencia educacional deve ser cadastrada')
def checa_educacao_cadastrada(context):
    wait = WebDriverWait(context.web, 3)
    context.resultado_busca_item1 = wait.until(ec.presence_of_element_located(
        (By.CLASS_NAME, 'experiencia-cadastrada')), message='Registro de "Experiencia Cadastrada" era esperado e não foi encontrado.')


@when(u'clico no botao de adicionar cadastro de Atuação Profissional')
def clica_adicionar_atuacao_profissional(context):
    context.adicionar_educacao = context.web.find_element_by_xpath(
        '//*[@id="root"]/div/div/section[2]/h2/button')
    context.adicionar_educacao.click()


@when(u'preencho a etapa de Atuação Profissional do formulario de cadastro')
def preenche_atuacao_profissional_formulario(context):
    context.organizacao_input = context.web.find_element_by_id('organizacao')
    context.organizacao_input.send_keys(name_generator())

    context.cargo_input = context.web.find_element_by_id('cargo')
    context.cargo_input.send_keys(name_generator())

    context.cargo_input = context.web.find_element_by_id('descricao')
    context.cargo_input.send_keys(name_generator())

    # Vínculo
    context.nivel_formacao_arrow = context.web.find_element_by_xpath(
        '//*[@id="root"]/div/div/section[2]/form/aside/section[2]/div/label/div/div/div[2]')
    context.nivel_formacao_arrow.click()

    context.nivel_formacao_input = context.web.find_element_by_id(
        'vinculo')
    context.nivel_formacao_input.send_keys('Freelance')

    wait = WebDriverWait(context.web, 3)
    wait.until(ec.element_to_be_clickable(
        (By.CSS_SELECTOR, 'div.react-select__menu')), message='Select de "Nível de Formação" era esperado e não foi encontrado.')

    context.nivel_formacao_selector = context.web.find_element_by_css_selector(
        'div.react-select__menu')

    context.nivel_formacao_option = context.web.find_element_by_xpath(
        '//div[contains(@class, "react-select__option")]')
    context.nivel_formacao_option.click()

    # Mês inicial
    context.month_input = context.web.find_element_by_id('initialMonth')
    context.month_input.send_keys(5)

    wait = WebDriverWait(context.web, 3)
    wait.until(ec.element_to_be_clickable(
        (By.CSS_SELECTOR, 'div.react-select__menu')), message='Select de "Mês inicial" era esperado e não foi encontrado.')

    context.month_option = context.web.find_element_by_xpath(
        '//div[contains(@class, "react-select__option")]')
    context.month_option.click()

    # Ano inicial
    context.month_input = context.web.find_element_by_id('initialYear')
    context.month_input.send_keys(1990)

    wait = WebDriverWait(context.web, 3)
    wait.until(ec.element_to_be_clickable(
        (By.CSS_SELECTOR, 'div.react-select__menu')), message='Select de "Ano inicial" era esperado e não foi encontrado.')

    context.month_option = context.web.find_element_by_xpath(
        '//div[contains(@class, "react-select__option")]')
    context.month_option.click()

    # Mês final
    context.month_input = context.web.find_element_by_id('finalMonth')
    context.month_input.send_keys(5)

    wait = WebDriverWait(context.web, 3)
    wait.until(ec.element_to_be_clickable(
        (By.CSS_SELECTOR, 'div.react-select__menu')), message='Select de "Mês final" era esperado e não foi encontrado.')

    context.month_option = context.web.find_element_by_xpath(
        '//div[contains(@class, "react-select__option")]')
    context.month_option.click()

    # Ano final
    context.month_input = context.web.find_element_by_id('finalYear')
    context.month_input.send_keys(1995)

    wait = WebDriverWait(context.web, 3)
    wait.until(ec.element_to_be_clickable(
        (By.CSS_SELECTOR, 'div.react-select__menu')), message='Select de "Ano final" era esperado e não foi encontrado.')

    context.month_option = context.web.find_element_by_xpath(
        '//div[contains(@class, "react-select__option")]')
    context.month_option.click()


@when(u'clico no botao de salvar cadastro de Atuação Profissional')
def clica_salvar_atuacao_profissional(context):
    context.salvar_atuacao_profissional = context.web.find_element_by_xpath(
        '//*[@id="root"]/div/div/section[2]/form/aside/section[5]/button[1]')
    context.salvar_atuacao_profissional.click()


@then(u'uma nova atuação profissional deve ser cadastrada')
def checa_atuacao_profissional_cadastrada(context):
    wait = WebDriverWait(context.web, 3)
    context.resultado_busca_item1 = wait.until(ec.presence_of_element_located(
        (By.CLASS_NAME, 'atuacao-profissional-cadastrada')), message='Registro de "Atuação Profissional" era esperado e não foi encontrado.')
