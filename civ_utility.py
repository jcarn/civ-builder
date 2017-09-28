from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def get_random_name():
    url = "http://www.fantasynamegenerators.com/country_names.php"

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    content = urlopen(req).read()

    soup = BeautifulSoup(content)

    print(soup.prettify())
    print(soup.find_all("result"))

get_random_name()

