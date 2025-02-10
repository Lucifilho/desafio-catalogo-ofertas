import re
from django.shortcuts import render, redirect
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from .models import Product

def get_products(request):
    driver = webdriver.Chrome()

    driver.get("https://www.mercadolivre.com.br/")

    pageTitle = driver.title

    elem = driver.find_element(By.NAME, "as_word")
    elem.clear()
    elem.send_keys("Computador Gamer i7 16gb ssd 1tb")

    search = driver.find_element(By.XPATH, "/html/body/header/div/div[2]/form/button")
    search.click()

    # Rolar a página para garantir que todos os elementos sejam carregados
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Aguarde o carregamento da página
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Espera explícita para garantir que as imagens estão visíveis
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "poly-component__picture")))

    elementsImage = driver.find_elements(By.CLASS_NAME, "poly-component__picture")
    elementsName = driver.find_elements(By.CLASS_NAME, "poly-component__title")
    elementsInstallment = driver.find_elements(By.CLASS_NAME, "poly-price__installments")
    elementsLink = driver.find_elements(By.CLASS_NAME, "poly-component__title")
    elementsPricePrevious = driver.find_elements(By.CSS_SELECTOR, ".andes-money-amount.andes-money-amount--previous.andes-money-amount--cents-comma")
    elementsEntirePrice = driver.find_elements(By.CSS_SELECTOR, ".poly-price__current .andes-money-amount.andes-money-amount--cents-superscript .andes-money-amount__fraction")
    elementsTypeShipping = driver.find_elements(By.CLASS_NAME, "poly-component__shipped-from")
    elementsFreeShipping = driver.find_elements(By.CLASS_NAME, "poly-component__shipping")
    elementsPercentualDiscount = driver.find_elements(By.CLASS_NAME, "andes-money-amount__discount")

    products = []
    for i in range(len(elementsName)):
        name = elementsName[i].text

        # Tentando pegar a imagem do atributo 'data-src' ou 'src'
        image = elementsImage[i].get_attribute('data-src') or elementsImage[i].get_attribute('src')

        # Verifica se a imagem foi carregada corretamente ou se é um placeholder
        if not image or image.startswith("data:image"):
            image = "https://via.placeholder.com/150"  # URL de placeholder

        url = elementsLink[i].get_attribute('href')
        pricePrevious = elementsPricePrevious[i].get_attribute("aria-label") if i < len(elementsPricePrevious) else None
        entire_price = elementsEntirePrice[i].text if i < len(elementsEntirePrice) else None


        installment_quantity = elementsInstallment[i].text if i < len(elementsInstallment) else None
        shipping_type = "Entrega Full" if i < len(elementsTypeShipping) and elementsTypeShipping[i].text else "Entrega Normal"
        free_shipping = "Frete Grátis" if i < len(elementsFreeShipping) else "Consulte o valor do frete"
        percentual_discount_text = elementsPercentualDiscount[i].text if i < len(elementsPercentualDiscount) else None
        percentual_discount = int(re.search(r'\d+', percentual_discount_text).group()) if percentual_discount_text else None

        # Criar o objeto Product com as informações obtidas


        product = Product(
            name=name,
            link=url,
            pricePrevious=pricePrevious,
            image=image,
            installment=installment_quantity,
            entire_price=entire_price,
            shipping_type=shipping_type,
            free_shipping=free_shipping,
            percentual_discount=percentual_discount,
        )
        product.save()
        products.append(product)

    driver.quit()

    return redirect('home')

def home(request):
    free_shipping_filter = request.GET.get('free_shipping', 'all')
    sort_option = request.GET.get('sort', 'default')

    products = Product.objects.all()

    if free_shipping_filter == 'Frete Grátis':
        products = products.filter(free_shipping="Frete Grátis")

    if sort_option == 'highest_price':
        products = products.order_by('-entire_price')
    elif sort_option == 'lowest_price':
        products = products.order_by('entire_price')
    elif sort_option == 'highest_discount':
        products = products.order_by('-percentual_discount')

    return render(request, 'catalog/catalog_offerings.html', {
        'pageTitle': 'Product Catalog',
        'products': products,
        'free_shipping_filter': free_shipping_filter,
        'sort_option': sort_option
    })