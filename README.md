# HDRI-Haven-Downloader
This is a small script to download multiple hdris from hdrihaven.com in the resolution of your choice (1k, 2k, 4k, 8k, 16k, 20k) and also has an option to downlaod 8K Tonedmapped JPG. Thumbnails are automatically downloaded when not downloading the 8k Tonemapped JPG.

## Setup
* Install Python.
* Open command line in the directory of the script (Shift + Right Mouse Click > Open Command Line Here).
* Run ```pip install -r requirements.txt```
* Run ```python scraper.py <Resolution> <Category> <TonemappedJPG Y/N>```

## How to use
For Example, if you want to download all  hdris belonging to Studio Category in 4k resolution with Tonemapped JPG.

Type ```python scraper.py 4k Studio Y```

**NOTE:** 
* Please use lowercase 'k' when typing the resolution. 
* Thumbnails are skipped when downloading Tonemapped JPGs. 

## Credits
This script is modified from the works of 
* https://github.com/Alzy/hdrihaven_dl.git
* https://github.com/ktkk/hdrihaven-downloader.git
