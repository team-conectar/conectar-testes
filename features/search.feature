#language: pt
Funcionalidade: Reaizar buscas no sistema

'''Eu como visitante (usuário sem cadastro) do Conectar desejo realizar buscas na plataforma'''

Cenario: Buscar todos os projetos estando deslogado
Dado acesso a pagina inicial do Conectar
Quando clico no botao de buscar
Entao projetos e pessoas devem ser retornadas

Cenario: Buscar todos os projetos estando logado
Dado acesso a pagina inicial do Conectar
Quando preencho o formulario de login com dados cadastrados na base
Quando clico no botao de logar
Quando preencho o campo de busca com um nome de pessoa/projeto existente
Quando clico no botao de buscar
Entao projetos e pessoas devem ser retornadas
