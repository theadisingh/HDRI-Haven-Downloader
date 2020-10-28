# Download all hdris from HDRIHaven

# Importing Modules
import requests
import os
from sys import argv
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.request import urlretrieve
from urllib.request import URLopener
from fake_useragent import UserAgent

# Arguments
name, resolution, category, tonemappedjpg = argv

#File Count
filesnum = 0

print(f"Resolution {resolution}")
print(f"Category: {category}")
print(f"Tonemapped JPG: {tonemappedjpg}")

ua = UserAgent()
opener = URLopener()
opener.addheader('User-Agent', ua.chrome)

url = 'https://hdrihaven.com/hdris/'
url_category = url + '?c=' + category

r = requests.get(url_category, allow_redirects=True, headers={'User-Agent': ua.chrome})
soup = BeautifulSoup(r.text, 'html.parser')

save_to = category+' HDRI'

try:
    os.mkdir(save_to)
except Exception as e:
    pass
os.chdir(save_to)

hdris = soup.select('#item-grid a')

for hdri in hdris:
    thumbnail = hdri.select('.thumbnail')[0]['data-src']
    href = urlparse(hdri['href'])
    filename = href.query[2:] + '_' + resolution
    new_filename = filename.replace(category+'&h=','')
    tonemapped = thumbnail.replace('/files/hdri_images/thumbnails/','')

    dl_url = 'https://hdrihaven.com/files/hdris/' + new_filename
    thumbnail_url = 'https://hdrihaven.com/' + thumbnail
    tonemapped_url = 'https://hdrihaven.com/files/hdri_images/tonemapped/8192/' + tonemapped
    
    print(f"\n{new_filename} - {dl_url}")

    try:
        print(f"{new_filename}.hdr downloading...")
        ext = '.hdr'
        opener.retrieve(dl_url + ext, new_filename + ext)
        filesnum+=1
    except Exception as e:
        print(f"{new_filename}.hdr download failed, trying .exr...")
        try:
            ext = '.exr'
            opener.retrieve(dl_url + ext, new_filename + ext)
            filesnum+=1
        except Exception as e:
            print(f"{new_filename} download failed. Continuing...\n")
            continue
    
    if (tonemappedjpg=='Y' or tonemappedjpg=='y' or tonemappedjpg=='Yes' or tonemappedjpg=='yes'):
        print(f"8K Tonemapped {tonemapped} downloading...")
        opener.retrieve(tonemapped_url, os.path.basename(tonemapped_url))
    else:
        print(f"Thumbnail downloading...")
        opener.retrieve(thumbnail_url, os.path.basename(thumbnail_url))

print(f"\nDownload completed. {filesnum} files downloaded.")
