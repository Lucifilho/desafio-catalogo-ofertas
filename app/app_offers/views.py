import re
from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from .models import Product

def home(request):
    driver = webdriver.Chrome()

    driver.get("https://www.mercadolivre.com.br/")

    pageTitle = driver.title

    elem = driver.find_element(By.NAME, "as_word")
    elem.clear()
    elem.send_keys("Computador Gamer i7 16gb ssd 1tb")

    search = driver.find_element(By.XPATH, "/html/body/header/div/div[2]/form/button")
    search.click()

    time.sleep(5)

    page_source = driver.page_source

    product_pattern = re.compile(r'"@type":"Product","name":"(.*?)","image":"(.*?)","brand":{.*?},"offers":{.*?"price":(.*?),"priceCurrency":"(.*?)","url":"(.*?)"}')
    products_data = product_pattern.findall(page_source)

    products = []
    for product_data in products_data:
        name, image, price, price_currency, url = product_data
        image = image.replace(r'\u002F', '/')
        product = Product(
            name=name,
            link=url,
            price=f"{price} {price_currency}",
            image=image
        )
        product.save()
        products.append(product)

    driver.quit()

    return render(request, 'catalog/catalog_offerings.html', {
        'pageTitle': pageTitle,
        'products': products
    })


def show_products(request):
    products = Product.objects.all()
    return render(request, 'catalog/catalog_offerings.html', {
        'pageTitle': 'Product Catalog',
        'products': products
    })