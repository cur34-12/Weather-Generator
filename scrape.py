from bs4 import BeautifulSoup
import requests

url = 'www.bom.gov.au/nsw/forecasts/sydneywaters.shtml'
r  = requests.get("http://" +url)
data = r.text
soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print(link.get('href'))