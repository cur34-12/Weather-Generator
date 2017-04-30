from bs4 import BeautifulSoup
import requests

url = 'www.bom.gov.au/nsw/forecasts/sydneywaters.shtml'
r  = requests.get("http://" +url)
data = r.text
soup = BeautifulSoup(data, 'html.parser')

daydivs = soup.findAll("div", { "class" : "day" })

texttogenerate = daydivs[:2]

soup.text

print(texttogenerate)