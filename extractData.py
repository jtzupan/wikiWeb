# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 10:32:42 2016

@author: johnzupan
"""

from bs4 import BeautifulSoup
import re
import urllib2

def extractData(url):
    '''extract the associated acts data from the artist's wikipedia page.
    url (str): the artist wiki link
    
    Returns: a tuple of (artist1 wikilink, artist1 name, artist2 wikilink, artist2 name)
    '''

    #pulls in html from wikipedia
    html = urllib2.urlopen(url).read()
    
    #prepares data and finds required sections
    data = BeautifulSoup(html)
    infobox = data.find_all('table', class_='infobox vcard plainlist')
    
    #uses regex to find theassocated acts names and wiki links
    #rePattern = re.compile(r'''<th scope="row">Associated acts</th>(.*)</td>''',re.DOTALL)
    rePattern = re.compile(r'''<th scope="row"><span class="nowrap">Associated acts</span></th>(.*)</a></td>''',re.DOTALL)
    associatedActsRaw = re.findall(rePattern, str(infobox))[0]
    
    associatedActsURL = re.findall(r'href="(/wiki.*?)"', associatedActsRaw)
    associatedActsName = re.findall(r'title="(.*?)">', associatedActsRaw)

    #creates the final tuple by combining artist name and wikilink    
    associatedActsTuple = zip(associatedActsURL, associatedActsName)
    
    return associatedActsTuple
