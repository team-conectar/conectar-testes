#language: pt
Funcionalidade: Cadastrar no sistema com um novo usuário

'''Eu como futuro usuário do Conectar desejo me cadastrar no sistema'''

Cenario: Cadastrar no sistema com um novo usuário
Dado acesso a pagina inicial do Conectar
Quando clico no botao de cadastro
Quando preencho a primeira etapa do formulario de cadastro com dados não cadastrados na base
Entao devo ser registrado na plataforma e enviado para a segunda etapa

Cenario: Preencher a segunda etapa do cadastro
Dado estou na pagina da segunda etapa do cadastro
Quando preencho a segunda etapa do formulario de cadastro
Entao devo ser redirecionado para a terceira etapa

Cenario: Preencher informações de Educação
Dado estou na pagina da terceira etapa do cadastro
Quando clico no botao de adicionar cadastro de Educação
Quando preencho a etapa de Educação do formulario de cadastro
Quando clico no botao de salvar cadastro de Educação
Entao uma nova experiencia educacional deve ser cadastrada

Cenario: Preencher informações de Atuação Profissional
Dado estou na pagina da terceira etapa do cadastro
Quando clico no botao de adicionar cadastro de Atuação Profissional
Quando preencho a etapa de Atuação Profissional do formulario de cadastro
Quando clico no botao de salvar cadastro de Atuação Profissional
Entao uma nova atuação profissional deve ser cadastrada

# TO-DO: Escrever cenário de Projetos