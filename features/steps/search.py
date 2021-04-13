from behave import given, when, then


@when(u'nao preencho nenhuma informacao no campo de busca')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: When nao preencho nenhuma informacao no campo de busca')


@when(u'clico no botao de buscar')
def clica_btn_busca(context):
    raise NotImplementedError(u'STEP: When clico no botao de buscar')


@then(u'projetos e pessoas devem ser retornadas')
def checa_retorno_projetos_pessoas(context):
    raise NotImplementedError(
        u'STEP: Then projetos e pessoas devem ser retornadas')
