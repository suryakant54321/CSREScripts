# Import packages
from bs4 import BeautifulSoup
import requests
url = "http://www.csre.iitb.ac.in/~alok/Convocation2017/"
# Get list of all URL's
r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "lxml")
# Get links in a list
links = []
for link in soup.find_all('a'):
    link = link.get('href')
    if link.endswith(".JPG"):
        links.append(link)

# Start Downloading
for pic in links:
    fullPath = url+pic
    print("Downloading %s"%(fullPath))
    f = open(pic,'wb')
    f.write(requests.get(fullPath).content)
    f.close()
#-------------------------------------------
# Author: Suryakant Sawant
# Date: 24 Aug. 2017
# Objective: Downloading files from a URL
# License: CC
#-------------------------------------------