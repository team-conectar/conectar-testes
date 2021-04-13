#language: pt
Funcionalidade: Logar no sistema com um usuário existente

'''Eu como usuário do Conectar desejo acessar a página inicial do sistema e logar com o meu usuário'''

Cenario: Logar no sistema com um usuário existente
Dado acesso a pagina inicial do Conectar
Quando preencho o formulario de login com dados cadastrados na base
Quando clico no botao de logar
Entao devo ser logado na plataforma

Cenario: Redirecionamento para o Explorar após login
Dado acesso a pagina inicial do Conectar
Quando preencho o formulario de login com dados cadastrados na base
Quando clico no botao de logar
Entao devo ser redirecionado para a página Explorar