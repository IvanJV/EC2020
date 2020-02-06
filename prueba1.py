from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

def WebScraper(search):
    i = 1
    soup = [1]
    products = []
    while len(soup) > 0:
        url_a = 'https://salcobrand.cl/search?resultsPerPage=25&page='
        url_b = '&terms='
        url_c = '&sortBy=relevance&filter[]='

        url = url_a + str(i) +  url_b + search + url_c

        opts = Options()
        opts.headless = True
        req = webdriver.Firefox(options=opts)
        req.get(url)
        # req.implicitly_wait(10)
        soup = BeautifulSoup(req.page_source,'html.parser')
        req.quit()
        soup = soup.findAll('span',class_='product-info truncate')
        for product in soup:
            products.append(product.text)

        i += 1

    return products

search = 'aspirina'
print(WebScraper(search))