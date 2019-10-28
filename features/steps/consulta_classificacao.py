from behave import given, when, then
from time import sleep
from behave.fixture import use_fixture_by_tag
from behave.log_capture import capture

import allure

#Variáveis com os elementos que iremos interagir na página
base_url = 'https://globoesporte.globo.com/'
element_menu = 'menu-button'
element_link_brasileirao = 'menu-item-title'
get_primeiro = '//*[@id="classificacao__wrapper"]/article/section[1]/div/table[1]/tbody/tr[1]/td[2]/strong'

@given(u'acesso a pagina inicial do globo esporte')
def step(context):
    context.web.get(base_url)
    context.print=print
    allure.attach(context.web.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
    
@when('clico no menu do brasileirao')
def step_impl(context):
    context.element_menu = context.web.find_element_by_class_name(element_menu)
    context.element_menu.click()
    context.element_link_brasileirao = context.web.find_element_by_class_name(element_link_brasileirao)
    context.element_link_brasileirao.click()
    allure.attach(context.web.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)

@when('classificacao e exibida')
def step_impl(context):
    context.get_primeiro = context.web.find_element_by_xpath(get_primeiro)
    allure.attach(context.web.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)

@then('devo saber quem e o primeiro colocado')
def step_impl(context):
    primeiro = context.get_primeiro.text
    print(primeiro)
    
    file = open("features/results/results.txt", 'r')
    content = file.readlines()
    content.append("\n" + primeiro)
    file = open("features/results/results.txt", 'w')
    file.writelines(content)
    allure.attach(context.web.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
    #file=open("features/results/results.txt", "w")
    #file.write(primeiro)
    sleep(3)
    