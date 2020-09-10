import requests
from bs4 import BeautifulSoup

server = 'http://103.126.12.226/Data/disk4/Hollywood/16-11-19/'

stack = []
queue = []

def download(site_url):

    data = requests.get(site_url)
    soup = BeautifulSoup(data.text)
    
    tags = soup('a')
    for tag in tags[1:]:
        link = tag.get('href', None)
        if not link.startswith(site_url):
            link = site_url+link
        if link.upper().endswith((".MKV", ".MP4", ".WEBM", ".AVI", ".MOV", ".AVCHD", ".FLV", ".WMV")):
            stack.append(link)
            print(link)
        elif link.endswith('/'):
            queue.append(link)

download(server)
for item in queue:
    download(item)

print('Downloadable links:', len(stack))
print('Root directories found', len(queue))

with open('ftp_links.txt', 'w') as f:
    for item in stack:
        f.write(item + '\n')