#!/usr/bin/python3

from bs4 import BeautifulSoup
import os
import urllib
from urllib.request import urlopen

BingXML_URL ="http://www.bing.com/HPImageArchive.aspx?"
page= urlopen(BingXML_URL).read()
BingXml =BeautifulSoup(page, "lxml")
Images = BingXml.find_all('image')
ImageURL ="https://www.bing.com" + Images[0].url.text
ImageName = Images[0].startdate + ".jpg"

urllib.urlretrieve(ImageURL, ImageName)