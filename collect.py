import os
import requests, time
from bs4 import BeautifulSoup

BASE_URL = 'http://www.kijiji.it/case/vendita/roma-annunci-roma/'
MAX_PAGE_NUM = 1992  

def addAds(url):

  r = requests.get(url)
  content = r.content
  soup = BeautifulSoup(content)
  results = soup.find_all(class_='item topad result')

  for res in results:
	processAllAds(res)
  results = soup.find_all(class_='item result')

  for res in results:
    processAllAds(res)

def processAllAds(advert):

	global advert_id
        folder=str(advert_id/500*500+1).zfill(6)+"-"+str(advert_id/500*500+500).zfill(6)
	if not os.path.exists("documents/documents-"+ folder):
                os.makedirs("documents/documents-" + folder)
        path=root+"/documents-"+folder+ "/"
        file= open(path+str(advert_id).zfill(6) + ".tsv", "w")

	titolo= advert.h3.contents[0].encode("utf-8")
	location= advert.find(class_="locale").contents[0].encode("utf-8")
	price= advert.h4.contents[0].encode("utf-8")
	url=advert.find(class_="cta")
	url=url["href"]
	description=advert.find(class_="description").contents[0].encode("utf-8")

	file.write(titolo + "\t" + location + "\t" + price + "\t" +url + "\t" + description )
	advert_id= advert_id+1
	return 0

print "\nConnecting..."
def processAllPages(baseURL, minPage=1, maxPage=1, delay=0.1):
  print "\nConnected."
  print ""
  for i in range(minPage, maxPage+1):
    print "Processing page: " + str(i)
    addAds(baseURL + "?p=" + str(i))
    time.sleep(delay)

advert_id=0
if not os.path.exists("documents"):
	os.makedirs("documents")
root="./documents/"
processAllPages(BASE_URL, 1, MAX_PAGE_NUM)

