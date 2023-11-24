import requests
from bs4 import BeautifulSoup
from lib import add
import re




url = "https://forum.supermamki.ru/viewtopic.php?f=100&t=30620" # change url to any of the threads


response = requests.get(url)


soup = BeautifulSoup(response.content, "html.parser")


preformat = (re.sub(" Сообщений: ", "",soup.select(".gensmall")[0].get_text()))[2:-2]

for i in range(0,int(preformat)):
    add(soup.select(".postauthor")[i].get_text(), soup.select(".postbody")[i].get_text())