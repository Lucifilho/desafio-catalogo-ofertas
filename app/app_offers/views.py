from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def home(request):


    driver = webdriver.Chrome()  # Inicializa o navegador Chrome para automação

    driver.get("https://www.mercadolivre.com.br/")  # Abre o site do Mercado Livre no navegador automatizado

    pageTitle = driver.title

    # Localiza o campo de pesquisa na página, que possui o atributo "name" com valor "as_word"
    elem = driver.find_element(By.NAME, "as_word")
    elem.clear()
    elem.send_keys("Computador Gamer i7 16gb ssd 1tb")  # Preenche o campo de pesquisa com o texto especificado

    search = driver.find_element(By.XPATH, "/html/body/header/div/div[2]/form/button")  # Encontra o botão de pesquisa pelo XPath
    search.click()

    return render(request, 'catalog/catalog_offerings.html', {'pageTitle': pageTitle})
