from behave import given, when, then

# Variável com a URL do site que iremos interagir.
base_url = 'https://globoesporte.globo.com/'

# Variáveis com os elementos que iremos interagir na página
element_menu = 'menu-button'
element_link_brasileirao = 'menu-item-title'
get_primeiro = '//*[@id="classificacao__wrapper"]/article/section[1]/div/table[1]/tbody/tr[1]/td[2]/strong'

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
    context.get_primeiro = context.web.find_element_by_xpath(get_primeiro)


@then(u'devo saber quem e o primeiro colocado')
def step_impl(context):
    primeiro = context.get_primeiro.text
    print(primeiro)

    #Salva o resultado da variável primeiro em um arquivo txt
    file = open("features/results.txt", 'r')
    content = file.readlines()
    content.append("\n" + primeiro)
    file = open("features/results/results.txt", 'w')
    file.writelines(content)

