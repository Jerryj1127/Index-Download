import requests
import urllib
from bs4 import BeautifulSoup
import time
start_time = time.time()


server = 'http://103.126.12.226/Data/disk4/Hollywood/16-11-19/'

links = []
directories = []

directories.append(server)

def download(site_url):

    html = urllib.request.urlopen(site_url).read()
    soup = BeautifulSoup(html,"html.parser")
    #           OR
    #data = requests.get(site_url)
    #soup = BeautifulSoup(data.text, "html.parser")
    
    tags = soup('a')
    for tag in tags[1:]:
        link = tag.get('href', None)
        if not link.startswith(site_url):
            link = site_url+link
        if link.upper().endswith((".MKV", ".MP4", ".WEBM", ".AVI", ".MOV", ".AVCHD", ".FLV", ".WMV", ".SRT")):
            links.append(link)
            print(link)
        elif link.endswith('/'):
            directories.append(link)

for item in directories:
    download(item)

print('Downloadable links:', len(links))
print('Root directories found', len(directories)-1)

with open('ftp_links.txt', 'w') as f:
    for item in links:
        f.write(item + '\n')

print("\n--- %s seconds ---" % (time.time() - start_time))