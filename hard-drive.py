from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq

my_url = 'http://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=-1&IsNodeId=1&Description=GTX&bop=And&Page=1&PageSize=36&order=BESTMATCH'

uclient = ureq(my_url)
page_html = uclient.read()
uclient.close()
page_soup = soup(page_html,"html.parser")

containers = page_soup.find_all("div" , {"class" : "item-container"})
#print(len(containers))

filename = "item-list.csv"
f = open(filename , "w")
headers ="brand , product_name , shipping\n"
f.write(headers)


#print(soup.prettify(containers[0]))

for container in containers:

    brand = container.div.div.a.img["title"]

    title = container.find_all("a" , {"class" : "item-title"})
    product_name = title[0].text

    ship = container.find_all("li",{"class" : "price-ship"})
    shipping = ship[0].text.strip()

    print(brand)
    print(product_name)
    print(shipping)

    f.write(brand + "," + product_name.replace("," , "|") + "," + shipping + "\n")

f.close()










