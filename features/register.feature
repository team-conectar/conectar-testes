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
Entao devo ser enviado para a terceira etapa