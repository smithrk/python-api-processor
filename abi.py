import getopt
import sys
import requests
import json
import export 
import helpers
import urllib
from BeautifulSoup import BeautifulSoup
import re
import pandas as pd
import numpy as np
import csv as csv
import time
import cPickle as pickle
import urllib2

mydict = {}
# list of domain names in a text file
fname = 'domains_list_v2.txt'
fhand = open(fname)
mydomains = list()
for line in fhand:
    pieces = line.split()
    domain = pieces[0]
    mydomains.append(domain)
    

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

testexpression = "*."+"po.st"
for i in mydomains:
    url = 'http://www.' + i
    time.sleep(2)
    try:
        html = opener.open(url).read()
        soup = BeautifulSoup(html)
        print url
        regexCheck = re.findall(testexpression, soup)
        print regexCheck
        try:
            title = soup.title.string
        except:
            title = ''
        mydict[url] = title
    except:
        mydict[url] = ''


print(mydict)