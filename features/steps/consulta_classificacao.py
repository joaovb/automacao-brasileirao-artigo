from behave import given, when, then

# Variável com a URL do site que iremos interagir.
base_url = 'https://globoesporte.globo.com/'

# Variáveis com os elementos que iremos interagir na página
element_menu = 'menu-button'
element_link_brasileirao = 'menu-item-title'

@given(u'acesso a pagina inicial do globo esporte')
def step_impl(context):
    context.web.get(base_url)

@when(u'clico no menu do brasileirao')
def step_impl(context):
    context.element_menu = context.web.find_element_by_class_name(element_menu)
    context.element_menu.click()
    context.element_link_brasileirao = context.web.find_element_by_class_name(element_link_brasileirao)
    context.element_link_brasileirao.click()

@when(u'classificacao e exibida')
def step_impl(context):
    raise NotImplementedError(u'STEP: When classificacao e exibida')


@then(u'devo saber quem e o primeiro colocado')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then devo saber quem e o primeiro colocado')

