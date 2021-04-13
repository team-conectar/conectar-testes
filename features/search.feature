#language: pt
Funcionalidade: Reaizar buscas no sistema

'''Eu como visitante (usuário sem cadastro) do Conectar desejo realizar buscas na plataforma'''

Cenario: Buscar todos os projetos
Dado acesso a pagina inicial do Conectar
Quando nao preencho nenhuma informacao no campo de busca
Quando clico no botao de buscar
Entao projetos e pessoas devem ser retornadas
